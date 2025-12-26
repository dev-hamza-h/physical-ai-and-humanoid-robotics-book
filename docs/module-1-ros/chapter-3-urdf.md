# Chapter 3: Describing Robots with URDF

Before we can simulate or control a robot, we need a way to describe its physical structure. The **Unified Robot Description Format (URDF)** is an XML-based format used in ROS to model a robot's physical properties.

## Core Components of URDF

A URDF file is made up of two key components: **links** and **joints**.

### Links

A **link** represents a rigid part of the robot, like a limb segment, a torso, or a gripper. Each link has its own coordinate frame. Key properties of a link include:

*   **`<visual>`**: Defines the visual appearance of the link (e.g., its shape, color, and texture). This is what you see in a simulator.
*   **`<collision>`**: Defines the collision geometry of the link. This is what the physics engine uses to calculate collisions. It's often a simplified version of the visual geometry for efficiency.
*   **`<inertial>`**: Defines the inertial properties of the link (mass, center of mass, and inertia tensor). This is crucial for realistic physics simulation.

### Joints

A **joint** connects two links and defines their relative motion. Each joint has a parent link and a child link. Key properties of a joint include:

*   **`type`**: The type of motion allowed. Common types include:
    *   `revolute`: A rotational joint with defined limits (e.g., an elbow).
    *   `continuous`: A rotational joint with no limits (e.g., a wheel).
    *   `prismatic`: A sliding joint with defined limits (e.g., a piston).
    *   `fixed`: A joint that does not allow any motion.
*   **`<parent>`** and **`<child>`**: The two links that the joint connects.
*   **`<origin>`**: The transform (position and orientation) of the child link relative to the parent link.
*   **`<axis>`**: The axis of rotation or translation for the joint.
*   **`<limit>`**: The motion limits for revolute and prismatic joints (e.g., upper and lower joint angles, velocity, and effort).

By linking together a series of links and joints, we can create a complete kinematic tree that describes the structure of our entire robot, from its base to its end-effectors.

## Example: A Simple Humanoid Leg

Here is a simplified URDF for a two-link humanoid leg, consisting of an upper leg and a lower leg connected by a knee joint.

```xml
<?xml version="1.0"?>
<robot name="simple_leg">

  <!-- Base Link -->
  <link name="base_link">
    <visual>
      <geometry>
        <box size="0.1 0.1 0.05" />
      </geometry>
    </visual>
  </link>

  <!-- Hip Joint -->
  <joint name="hip_joint" type="fixed">
    <parent link="base_link"/>
    <child link="upper_leg"/>
    <origin xyz="0 0 0.5"/>
  </joint>

  <!-- Upper Leg Link -->
  <link name="upper_leg">
    <visual>
      <geometry>
        <cylinder length="0.4" radius="0.05" />
      </geometry>
      <origin xyz="0 0 -0.2" rpy="0 0 0" />
    </visual>
    <collision>
      <geometry>
        <cylinder length="0.4" radius="0.05" />
      </geometry>
      <origin xyz="0 0 -0.2" rpy="0 0 0" />
    </collision>
    <inertial>
      <mass value="1.0" />
      <inertia ixx="1.0" ixy="0.0" ixz="0.0" iyy="1.0" iyz="0.0" izz="1.0" />
    </inertial>
  </link>

  <!-- Knee Joint -->
  <joint name="knee_joint" type="revolute">
    <parent link="upper_leg"/>
    <child link="lower_leg"/>
    <origin xyz="0 0 -0.4" />
    <axis xyz="0 1 0" />
    <limit lower="0" upper="2.6" effort="100" velocity="10"/>
  </joint>

  <!-- Lower Leg Link -->
  <link name="lower_leg">
    <visual>
      <geometry>
        <cylinder length="0.3" radius="0.04" />
      </geometry>
      <origin xyz="0 0 -0.15" rpy="0 0 0" />
    </visual>
    <collision>
      <geometry>
        <cylinder length="0.3" radius="0.04" />
      </geometry>
      <origin xyz="0 0 -0.15" rpy="0 0 0" />
    </collision>
    <inertial>
      <mass value="0.7" />
      <inertia ixx="1.0" ixy="0.0" ixz="0.0" iyy="1.0" iyz="0.0" izz="1.0" />
    </inertial>
  </link>

</robot>
```

This URDF defines a `base_link`, an `upper_leg` link, and a `lower_leg` link. The `hip_joint` is fixed, while the `knee_joint` is a revolute joint that allows rotation around the Y-axis, mimicking a simple knee. This forms the basis for building more complex humanoid structures.
