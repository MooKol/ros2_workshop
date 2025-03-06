from typing import Callable, List
import rclpy
from rclpy.callback_groups import CallbackGroup
from rclpy.clock import Clock            
from rclpy.node import Node
from rclpy.timer import Timer
from std_msgs.msg import String

class SimplePublisher(Node):
        def __init__ (self):
                super().__init__("simple_publisher")
                self.pub_ = self.create_publisher(String, "Chatter", 5)
                self.counter_ = 0
                self.frequency_ = 2.0 #Hz
                self.get_logger().info("publishing at %d Hz" % self.frequency_)
                self.timer = self.create_timer(self.frequency_, self.timerCallback)
        print("hello world")

        def timerCallback(self):
                msg = String ()
                msg.data = "Hello Ros2 - counter %d" % self.counter_
                self.pub_.publish(msg)
                self.counter_ +=1

def main():
        rclpy.init()
        simple_publisher = SimplePublisher()
        rclpy.spin(simple_publisher)  ## Keep the node active and the time and node running
        simple_publisher.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
        main()
