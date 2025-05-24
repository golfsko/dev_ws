from setuptools import find_packages, setup

package_name = 'my_cutter_bridge'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='golfsko',
    maintainer_email='nyegolfsko@hotmai.com',
    description='Bridge node to send cutter commands to Arduino',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'bridge = my_cutter_bridge.cutter_bridge:main', 
            'joy_to_cutter = my_cutter_bridge.joy_to_cutter:main',
        ],
    },
)
