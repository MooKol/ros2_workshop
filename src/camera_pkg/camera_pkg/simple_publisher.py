import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):
    def __init__(self):
        super().__init__('simple_publisher')
        self.pub_ = self.create_publisher(String, 'camera_topic', 10)
        self.cout_ = 0
        self.frequency_ = 100 # 1 Hz
        self.timer_ = self.create_timer(1.0 / self.frequency_, self.msgCallback)

    def msgCallback(self):
        msg = String()
        msg.data = 'Hello World! %d' % self.cout_
        self.pub_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.cout_ += 1

def main():
    rclpy.init()
    simple_publisher = SimplePublisher()
    rclpy.spin(simple_publisher)
    simple_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__': 
    main()