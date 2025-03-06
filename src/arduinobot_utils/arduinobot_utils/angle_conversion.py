#!/usr/bin/env python3


import rclpy
from rclpy.node import Node
from arduinobot_msgs.srv import EulerToQuaternion, QuaternionToEuler
from tf_transformations import quaternion_from_euler, euler_from_quaternion

class AnglesConverter(Node):
    def __init__(self):
        super().__init__("angle_conversion_setvice_server")

        self.euler_to_quaternion_ = self.create_service(EulerToQuaternion,"euler_to_quaternion", self.eulerToQuaternionCallback)
        self.quaternion_to_euler_ = self.create_service(QuaternionToEuler,"quaternion_to_euler", self.quaternionToEulerCallback)

        self.get_logger().info("Angle Conversions are Ready")

    def eulerToQuaternionCallback(self, req, res):
        self.get_logger().info("Requested to convert euler angels roll: %f, pitch:%f, yaw:%f, into Quaternion."
                                % (req.roll, req.pitch, req.yaw))
        (res.x, res.y, res.z, res.w) = quaternion_from_euler(req.roll, req.pitch, req.yaw)
        self.get_logger().info("Coressponding quaternion: x:%f, y: %f, z: %f, w:%f")
        return res
    
    def quaternionToEulerCallback(self, req, res):
        self.get_logger().info("Requested to convert quaternion Qngels x: %f, y:%f, z:%f, w:%f into Euler"
                               %(req.x, req.y, req.z, req.w))
        (res.roll, res.pitch, res.yaw) = euler_from_quaternion (req.x, req.y, req.z, req.w)
        self.get_logger().info("Coressponding quaternion: roll: %f, pitch: %f, yaw: %f")
        return res

def main():
        rclpy.init()
        angles_converter = AnglesConverter()
        rclpy.spin(angles_converter)  ## Keep the node active and the time and node running
        angles_converter.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
        main()
