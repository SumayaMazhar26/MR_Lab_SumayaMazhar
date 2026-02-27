import rclpy
from rclpy.node import Node
import os

class SimpleNode(Node):

    def __init__(self):
        super().__init__('simple_node')

        file_path = os.path.join(os.path.dirname(__file__), "counter.txt")

        with open(file_path, "r") as f:
            count = int(f.read())

        count += 1

        with open(file_path, "w") as f:
            f.write(str(count))

        self.get_logger().info(f"Run count: {count}")


def main(args=None):
    rclpy.init(args=args)
    node = SimpleNode()

    rclpy.spin_once(node, timeout_sec=0.1)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
