import rclpy
from rclpy.node import Node


class SimpleNode(Node):

    def __init__(self):
        super().__init__('simple_node')

        # Declare parameter with default value None
        self.declare_parameter('student_name', None)

        # Get parameter value
        name = self.get_parameter('student_name').value

        # Check if parameter is set
        if name:
            self.get_logger().info(f'Student name: {name}')
        else:
            self.get_logger().info('student_name not set')


def main(args=None):
    rclpy.init(args=args)
    node = SimpleNode()
    rclpy.spin_once(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()

