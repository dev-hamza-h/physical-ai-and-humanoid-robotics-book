# Chapter 1: Simulating Humanoids in Gazebo

Gazebo is a powerful and widely-used robotics simulator that excels at one thing in particular: physics. In this chapter, we'll explore how to set up a Gazebo world and simulate the complex physics of a humanoid robot.

## Why Gazebo for Physics?

While other simulators might offer better graphics, Gazebo's strength lies in its robust and realistic physics engine. It can simulate:

*   **Gravity**: A fundamental force that dictates how our robot interacts with the world.
*   **Collisions**: Gazebo's detailed collision modeling allows us to simulate contact between the robot's feet and the ground, or between its hands and an object.
*   **Joint Constraints**: It respects the joint limits and forces defined in our URDF, preventing the robot from moving in unrealistic ways.
*   **Inertia and Mass**: The inertial properties of each link are used to calculate how forces and torques affect the robot's motion. This is critical for stable walking and balance.

## The Gazebo World File

A Gazebo simulation is defined in a `.world` file, which is an XML file that specifies everything in the environment:

*   **The Scene**: Lighting, sky, and global physics parameters like gravity.
*   **Objects**: Static objects like ground planes, walls, tables, and other obstacles.
*   **Robots**: One or more robot models, typically included from a URDF file.
*   **Plugins**: Gazebo plugins can be used to add custom functionality, like sensor data generation or interfaces to ROS 2.

For a humanoid, a good starting world includes a ground plane and not much else. This allows us to focus on the robot's stability and movement without worrying about complex obstacles.

## Tutorial: A Simple Gazebo World

Let's create a world file that includes a ground plane and our simple leg URDF from the previous chapter.

### 1. The World File (`simple_world.world`)

```xml
<?xml version="1.0" ?>
<sdf version="1.6">
  <world name="default">

    <!-- A global light source -->
    <include>
      <uri>model://sun</uri>
    </include>

    <!-- A ground plane -->
    <include>
      <uri>model://ground_plane</uri>
    </include>

    <!-- Physics Engine Configuration -->
    <physics type="ode">
      <max_step_size>0.001</max_step_size>
      <real_time_factor>1</real_time_factor>
      <real_time_update_rate>1000</real_time_update_rate>
    </physics>

    <!-- Spawn our robot -->
    <include>
      <name>simple_leg</name>
      <uri>model://path/to/your/simple_leg_urdf_folder</uri> <!-- IMPORTANT: Update this path -->
    </include>

  </world>
</sdf>
```

**IMPORTANT**: Before you can use your URDF in Gazebo, you need to turn it into a Gazebo "model". This typically involves creating a `model.config` file and a folder structure that Gazebo understands. For now, just know that the `<uri>` tag will point to this model folder.

### 2. Launching the World

To launch this world, you can use a ROS 2 launch file. The launch file will start Gazebo and spawn your robot model into the simulated environment.

```python
# In your launch file
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose', 'path/to/your/simple_world.world'],
            output='screen'
        ),
        Node(
            package='your_package_name',
            executable='spawn_robot_entity',
            arguments=['-entity', 'simple_leg', '-file', 'path/to/your/simple_leg.urdf'],
            output='screen'
        )
    ])
```

When you run this launch file, Gazebo will open, and you will see your simple leg model standing on a ground plane, ready to be simulated. This is the starting point for all our physics-based experiments.
