# Chapter 1: ROS 2 Core Concepts

Welcome to the core of the Robotic Nervous System. In this chapter, we'll explore the fundamental building blocks of ROS 2: Nodes, Topics, and Services.

## ROS 2 Nodes

A **node** is the primary building block of a ROS 2 system. Think of a node as a small, single-purpose program within a larger robotics application. For example, you might have one node for controlling the wheel motors, another for reading laser scanner data, and a third for planning a path.

Each node should be responsible for a single, well-defined task. This modularity makes your system easier to debug, test, and scale.

## ROS 2 Topics

**Topics** are the buses that nodes use to exchange data. They are named channels over which nodes can send and receive messages. Topics use a publish/subscribe model:

*   A **publisher** is a node that sends messages to a topic.
*   A **subscriber** is a node that receives messages from a topic.

Many nodes can publish or subscribe to the same topic. This allows for a flexible, decoupled architecture where nodes don't need to know about each other's existence.

### Example: A Simple Talker and Listener

Here's a conceptual example:

*   A `camera_node` publishes images to an `/image_raw` topic.
*   A `vision_node` subscribes to `/image_raw` to detect objects.
*   A `display_node` also subscribes to `/image_raw` to show the video feed on a screen.

## ROS 2 Services

While topics are for continuous data streams, **services** are used for request/response interactions. A service has two parts:

*   A **service server** (or provider) offers a specific capability.
*   A **service client** requests that capability and waits for a response.

Unlike topics, services are synchronous. The client sends a request and waits until the server has completed the task and returned a result.

### Example: A "Reboot Robot" Service

*   A `hardware_manager_node` provides a `/reboot` service.
*   An `emergency_stop_node` can call this service to reboot the robot if it detects a critical error. The `emergency_stop_node` will wait for a confirmation that the reboot process has started.

## Tutorial: Your First Publisher and Subscriber

Let's make this concrete with some Python code. We'll create two nodes: one that publishes a "Hello, World!" message and another that subscribes to it.

### 1. The Publisher Node (`talker.py`)

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TalkerNode(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello World: {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    node = TalkerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

### 2. The Subscriber Node (`listener.py`)

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ListenerNode(Node):
    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = ListenerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

### 3. Running the Nodes

To run this example, you would save each file, build your ROS 2 workspace, and then run each node in a separate terminal:

**Terminal 1:**
```bash
ros2 run your_package_name talker
```

**Terminal 2:**
```bash
ros2 run your_package_name listener
```

You will see the "talker" publishing messages and the "listener" receiving them. This simple example demonstrates the power of the publish/subscribe model for decoupled communication.
