import rclpy
import keyboard
import json
from rclpy.node import Node
from std_msgs.msg import String


class CommandPublisher(Node):

    def __init__(self):
        super().__init__('command_publisher')
        self.publisher = self.create_publisher(String, 'commands', 10)

        # get key state
        keyboard.on_press_key("up", self.goForward)
        keyboard.on_release_key("up", self.linearStop)

        keyboard.on_press_key("down", self.goBackward)
        keyboard.on_release_key("down", self.linearStop)

        keyboard.on_press_key("left", self.turnLeft)
        keyboard.on_release_key("left", self.angularStop)

        keyboard.on_press_key("right", self.turnRight)
        keyboard.on_release_key("right", self.angularStop)

    def publish(self, jsonString):
        msg = String()
        msg.data = str(jsonString)
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg)

    def goForward(self, e):
        data = {
            "Command": "SetLinearSpeed",
            "Payload": {
                "velX": 0.4
            }
        }
        data = json.dumps(data)
        self.publish(data)

    def linearStop(self, e):
        data = {
            "Command": "SetLinearSpeed",
            "Payload": {
                "velX": 0.0
            }
        }
        data = json.dumps(data)
        self.publish(data)

    def goBackward(self, e):
        data = {
            "Command": "SetLinearSpeed",
            "Payload": {
                "velX": -0.4
            }
        }
        data = json.dumps(data)
        self.publish(data)

    def turnLeft(self, e):
        data = {
            "Command": "SetAngularSpeed",
            "Payload": {
                "velrz": -150.0
            }
        }
        data = json.dumps(data)
        self.publish(data)

    def turnRight(self, e):
        data = {
            "Command": "SetAngularSpeed",
            "Payload": {
                "velrz": 150.0
            }
        }
        data = json.dumps(data)
        self.publish(data)

    def angularStop(self, e):
        data = {
            "Command": "SetAngularSpeed",
            "Payload": {
                "velrz": 0.0
            }
        }
        data = json.dumps(data)
        self.publish(data)

def main(args=None):
    rclpy.init(args=args)

    commandPublisher = CommandPublisher()

    rclpy.spin(commandPublisher)

    commandPublisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
