// The turtle in turtlesim will move in a circle!!
// Terminal 1: ros2 run turtlesim turtlesim_node
// Terminal 2 (this one, with the venv active): python turtle_circle.py


import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class CircleDriver(Node):
    def __init__(self):
        super().__init__('circle_driver')
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.tick)

    def tick(self):
        msg = Twist()
        msg.linear.x = 2.0   # forward speed
        msg.angular.z = 1.0  # turning speed
        self.pub.publish(msg)


def main():
    rclpy.init()
    node = CircleDriver()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()