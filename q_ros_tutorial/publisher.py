from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile

import time

def create_twist(linear, angular):
    twist = Twist()
    twist.linear.x = linear
    twist.linear.y = 0.0
    twist.linear.z = 0.0
    twist.angular.x = 0.0
    twist.angular.y = 0.0
    twist.angular.z = angular
    return twist


class TwistPublisher(Node):

    def __init__(self):
        super().__init__('twist_publisher')

        qos = QoSProfile(depth=10)
        self._publisher = self.create_publisher(Twist, '/simplebot/cmd_vel', qos)

        time.sleep(0.2)
        
        twist = create_twist(0.3, 0.0)
        self._publisher.publish(twist)
        print('START')

        stop_timer_period = 15
        self._stop_timer = self.create_timer(stop_timer_period, self.stop)
        

    def stop(self):
        if self._stop_timer:
            self.destroy_timer(self._stop_timer)
            self._stop_timer = None

        twist = create_twist(0.0, 0.0)
        self._publisher.publish(twist)
        print('STOP')

def main(args=None):

    try:
        rclpy.init(args=args)
        twist_publisher = TwistPublisher()
        rclpy.spin(twist_publisher)
    except KeyboardInterrupt as identifier:
        pass
    finally:
        twist_publisher.stop()
        time.sleep(1)
        twist_publisher.destroy_node()  
        rclpy.shutdown()
    

if __name__ == "__main__":
    main()
    


