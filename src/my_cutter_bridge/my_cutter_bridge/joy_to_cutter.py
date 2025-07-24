import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import Int32

class JoyToCutter(Node):
    def __init__(self):
        super().__init__('joy_to_cutter')
        self.subscription = self.create_subscription(Joy, '/joy', self.joy_callback, 10)
        self.publisher = self.create_publisher(Int32, '/cutter_cmd', 10)
        self.prev_button_state = 0
        self.cutter_on = False
        self.button_index = 2  # change this to match your remote

    def joy_callback(self, msg):
        button_state = msg.buttons[self.button_index]
        if button_state == 1 and self.prev_button_state == 0:
            self.cutter_on = not self.cutter_on
            speed = 40 if self.cutter_on else 0
            self.publisher.publish(Int32(data=speed))
            self.get_logger().info(f'Cutter {"ON" if self.cutter_on else "OFF"}')

        self.prev_button_state = button_state

def main(args=None):
    rclpy.init(args=args)
    node = JoyToCutter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()