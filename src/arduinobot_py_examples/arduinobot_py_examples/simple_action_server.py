import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from arduinobot_msgs.action import Fibonacci
import time


class SimpleActionServer(Node):
    def __init__(self):
        super().__init__("simple_action_server")
        self.get_logger().info("Starting the Server")
        self.action_server = ActionServer(self, Fibonacci, "fibonacci", self.goalCallback)

    def goalCallback(self, goal_handle):
        self.get_logger().info("Received goal request with order %d" % goal_handle.request.order)
        feedback_msg = Fibonacci.Feedback()
        feedback_msg.partial_sequance = [0, 1]

        for i in range(1, goal_handle.request.order):
            feedback_msg.partial_sequance.append(
                feedback_msg.partial_sequance[i] + feedback_msg.partial_sequance[i - 1]
            )
            self.get_logger().info("Feedback: {0}".format(feedback_msg.partial_sequance))

            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)

        goal_handle.succeed()

        result = Fibonacci.Result()
        result.sequence = feedback_msg.partial_sequance
        return result 


def main(args=None):
    rclpy.init(args=args)
    simple_action_server = SimpleActionServer()
    rclpy.spin(simple_action_server)


if __name__ == "__main__":
    main()