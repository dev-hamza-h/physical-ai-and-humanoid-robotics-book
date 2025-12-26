# Chapter 2: Bridging Python Agents to ROS 2 with `rclpy`

In the world of AI, an "agent" is an entity that perceives its environment and acts upon it. In this chapter, we'll learn how to create a Python-based agent and connect it to a ROS 2 system using the `rclpy` library.

## The Role of `rclpy`

`rclpy` is the official Python client library for ROS 2. It provides the necessary tools to create nodes, publish and subscribe to topics, and use services and actions—all from within a standard Python script. This is the bridge that allows our AI logic to communicate with the rest of the robot.

## Agent-Based Architecture

Why use an "agent" architecture?

*   **Separation of Concerns**: We can separate the high-level decision-making logic (the "brain") from the low-level hardware control. The agent decides *what* to do, and the ROS 2 controllers handle *how* to do it.
*   **Modularity**: The agent can be developed and tested independently of the robot's hardware.
*   **Flexibility**: We can easily swap out different agent models (e.g., a simple rule-based agent for a complex neural network) without changing the underlying ROS 2 system.

## Connecting the Agent to ROS 2

The most common pattern is to create a ROS 2 node that wraps our Python agent. This node is responsible for:

1.  **Subscribing to sensor data**: The agent needs information about the environment. The wrapper node subscribes to topics (e.g., `/camera/image_raw`, `/laser_scan`) and passes the data to the agent.
2.  **Passing data to the agent**: The agent's "perceive" function takes in the sensor data and decides on an action.
3.  **Publishing commands**: The wrapper node takes the agent's chosen action and publishes it as a message on a ROS 2 topic (e.g., `/cmd_vel`) or uses an action server for more complex tasks.

## Tutorial: Agent Controlling a ROS 2 Action

Actions are like services but for long-running tasks. They provide feedback while the task is executing. Let's create an agent that tells a robot to move a certain distance using an action.

### 1. The Action Definition (`Move.action`)

First, we define the action in a `.action` file:

```
# Goal
float32 distance
---
# Result
bool success
---
# Feedback
float32 distance_traveled
```

### 2. The Action Server (The Robot's Controller)

The action server would be part of the robot's control system. It receives the goal, moves the robot, and provides feedback. (The full code for the server is omitted here for brevity, but it would involve moving the robot and publishing feedback).

### 3. The Agent and its Wrapper Node

Here's the Python agent and the ROS 2 node that wraps it.

```python
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from your_action_package.action import Move  # Import your custom action

class MoveAgent:
    def decide_action(self):
        # In a real agent, this would be based on sensor data.
        # Here, we'll just command it to move 1.0 meter.
        return 1.0

class AgentWrapperNode(Node):
    def __init__(self, agent):
        super().__init__('agent_wrapper')
        self.agent = agent
        self._action_client = ActionClient(self, Move, 'move_robot')
        self.timer = self.create_timer(5.0, self.run_agent) # Run agent every 5s

    def run_agent(self):
        distance = self.agent.decide_action()
        self.send_goal(distance)

    def send_goal(self, distance):
        goal_msg = Move.Goal()
        goal_msg.distance = distance

        self.get_logger().info('Waiting for action server...')
        self._action_client.wait_for_server()

        self.get_logger().info(f'Sending goal request: move {distance} meters')
        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback)

        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f'Result: {result.success}')
        
    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(f'Received feedback: Traveled {feedback.distance_traveled} meters')


def main(args=None):
    rclpy.init(args=args)
    agent = MoveAgent()
    agent_wrapper = AgentWrapperNode(agent)
    rclpy.spin(agent_wrapper)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

### 4. Running the System

1.  Run the action server (the robot's controller).
2.  Run the agent wrapper node.

The agent will decide to move, and the wrapper node will send the goal to the action server. The server will then execute the movement, and the agent wrapper will receive feedback and the final result.
