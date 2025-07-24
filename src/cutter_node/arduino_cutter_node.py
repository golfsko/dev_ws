import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import serial

class CutterBridge(Node):
    def __init__(self):
        super().__init__('cutter_bridge')

        # Adjust your serial port & baud rate here:
        self.serial_port = serial.Serial('/dev/ttyUSB0', 57600, timeout=1)

        self.subscription = self.create_subscription(
            Int32,
            'cutter_cmd',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        speed = max(0, min(20, msg.data))  # Clamp speed 0-100
        command = f'f {speed}\n'
        self.get_logger().info(f'Sending to Arduino: {command.strip()}')
        self.serial_port.write(command.encode())

def main(args=None):
    rclpy.init(args=args)
    node = CutterBridge()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
