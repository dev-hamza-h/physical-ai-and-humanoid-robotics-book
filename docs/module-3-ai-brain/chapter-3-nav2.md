# Chapter 3: Humanoid Path Planning with Nav2

The ROS 2 Navigation Stack (Nav2) is the standard and most powerful tool for mobile robot navigation. While it was primarily designed for wheeled robots, we can adapt it for bipedal humanoids, though we need to be aware of some significant challenges.

## Nav2 for Humanoids: The Core Idea

The core of Nav2 can still be used for a humanoid. The process looks like this:

1.  **Localization**: An algorithm like VSLAM (from the previous chapter) provides the robot's position in the map.
2.  **Path Planning**: Nav2's global planner (e.g., A*) finds a 2D path from the robot's current position to the goal, avoiding obstacles in the costmap.
3.  **Path Following**: This is where things get tricky. A standard Nav2 controller outputs `Twist` messages (linear and angular velocity). A humanoid robot cannot directly follow these commands. We need a special "path follower" or "locomotion controller."

## The Challenge: Bipedal Locomotion

The key challenge is translating a 2D path into stable walking motion for a bipedal robot. This is an active area of robotics research, but the general approach is to have a dedicated locomotion controller that:

1.  **Receives the 2D path** from Nav2.
2.  **Generates stable walking patterns**: It uses techniques like Zero Moment Point (ZMP) or Model Predictive Control (MPC) to generate a sequence of foot placements and joint trajectories that will allow the robot to follow the path without falling over.
3.  **Sends commands to the joints**: The locomotion controller sends the calculated joint commands to the robot's motors.

So, while we use Nav2 for high-level planning, we need a custom controller for low-level execution.

## Current Approaches

*   **Custom Path Follower Node**: You can create a custom ROS 2 node that subscribes to the path from Nav2 and implements your own locomotion control logic. This gives you the most flexibility.
*   **Specialized Humanoid Stacks**: Some research labs and companies have developed complete navigation stacks specifically for humanoids (e.g., the one used by Boston Dynamics' Atlas). These are often proprietary but provide a glimpse into the state-of-the-art.

For this book, we will focus on the first approach: using Nav2 for global planning and then outlining the requirements for a custom path follower that can be integrated with it.

## Tutorial: Basic Nav2 Setup for a Humanoid

This tutorial outlines how to configure Nav2 to generate a global path for a humanoid-like robot in a simulated environment.

### 1. The Configuration File (`nav2_params.yaml`)

You'll need a YAML file to configure the Nav2 plugins. For a humanoid, we are primarily interested in the global planner.

```yaml
planner_server:
  ros__parameters:
    use_sim_time: True
    planner_plugins: ["GridBased"]
    GridBased:
      plugin: "nav2_navfn_planner/NavfnPlanner"
      tolerance: 0.5
      use_astar: false

# We will not use the Nav2 controller_server, as it generates Twist commands.
# Instead, we will write our own path follower.
# controller_server:
#   ros__parameters:
#     ...

# Other Nav2 servers (smoother, behavior server) can be configured as needed.
```

### 2. The Launch File

Your launch file will start the Nav2 planner server and the lifecycle manager.

```python
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    nav2_yaml = os.path.join(get_package_share_directory('your_package_name'), 'config', 'nav2_params.yaml')

    return LaunchDescription([
        Node(
            package='nav2_planner',
            executable='planner_server',
            name='planner_server',
            output='screen',
            parameters=[nav2_yaml]
        ),
        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_path_planning',
            output='screen',
            parameters=[{'use_sim_time': True},
                        {'autostart': True},
                        {'node_names': ['planner_server']}]
        )
    ])
```

### 3. Running the System

1.  **Launch your simulation** with the robot and a map (e.g., from a VSLAM run).
2.  **Launch the Nav2 launch file** shown above.
3.  **Send a goal** to Nav2 using RViz or the command line.

You will see the planner server generate a path (a `nav_msgs/Path` message) and publish it. Your custom humanoid path follower node would subscribe to this topic.

This setup effectively decouples the high-level path planning from the low-level locomotion control, allowing you to leverage the power of Nav2 for global navigation while implementing custom, stable walking for your humanoid.
