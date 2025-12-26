# Chapter 2: High-Fidelity Rendering with Unity

While Gazebo is our workhorse for physics, Unity is our artist's studio. Unity is a professional game engine that offers stunning graphics and a rich ecosystem for creating interactive 3D environments. In this chapter, we'll learn how to use Unity to create a visually impressive digital twin of our robot.

## Why Unity for Rendering?

*   **Photorealistic Graphics**: Unity's rendering pipeline can produce beautiful, lifelike scenes with advanced lighting, shadows, and materials.
*   **Rich Asset Store**: The Unity Asset Store provides a massive library of 3D models, textures, and tools that can be used to build detailed and engaging virtual worlds.
*   **Human-Robot Interaction (HRI)**: Unity's built-in tools for creating user interfaces and handling user input make it an excellent platform for developing HRI scenarios, such as controlling the robot with a VR headset or interacting with virtual objects.

## The ROS-Unity Bridge

To connect Unity to our ROS 2 system, we use a "ROS bridge." The official [ROS-TCP-Connector](https://github.com/Unity-Technologies/ROS-TCP-Connector) from Unity is a set of packages that allow Unity to communicate with ROS 2 over a TCP connection.

This bridge allows us to:

*   **Publish data from Unity to ROS 2**: We can create a virtual camera in Unity and publish the image data to a ROS 2 topic, just like a real camera.
*   **Subscribe to data from ROS 2 in Unity**: We can subscribe to the robot's joint states from a ROS 2 topic and use that data to animate the robot model in Unity.

This creates a powerful "co-simulation" environment where Gazebo handles the physics while Unity provides a beautiful and interactive visualization. The robot's state is synchronized between the two simulators via ROS 2.

## Tutorial: Importing a URDF and Connecting to ROS 2

Here are the high-level steps to get your robot model from a URDF file into Unity and hooked up to ROS 2.

### 1. Import the URDF into Unity

Unity does not natively support URDF. You will need a special tool to import it. The [URDF-Importer-for-Unity](https://github.com/Unity-Technologies/URDF-Importer-for-Unity) is a Unity package that can parse a URDF file and automatically generate a corresponding robot model prefab in your Unity project.

1.  **Install the URDF Importer** package in your Unity project.
2.  **Import your URDF file**: Use the importer to select your robot's `.urdf` file. The importer will parse the file and create a hierarchy of GameObjects that represent your robot's links and joints.
3.  **Refine the Model**: The importer does a good job, but you may need to manually adjust materials, textures, and collision shapes to get the visual appearance you want.

### 2. Set up the ROS-TCP-Connector

1.  **Install the ROS-TCP-Connector** package in your Unity project.
2.  **Configure the ROS connection**: Create a GameObject in your scene to manage the ROS connection. You'll need to specify the IP address of the machine running your ROS 2 master.
3.  **Add ROS Publisher/Subscriber components**: Add the appropriate ROS components to your GameObjects. For example, to animate the robot, you would add a "ROS Subscriber" component to the root GameObject of your robot model. This component will subscribe to the `/joint_states` topic and apply the received joint angles to the corresponding joints in the Unity model.

### 3. A Simple Joint State Subscriber Script

Here's a simplified C# script that you would attach to your robot in Unity to subscribe to joint states and update the model.

```csharp
using UnityEngine;
using Unity.Robotics.ROSTCPConnector;
using RosMessageTypes.Sensor;

public class JointStateSubscriber : MonoBehaviour
{
    void Start()
    {
        // Subscribe to the /joint_states topic
        ROSConnection.GetOrCreateInstance().Subscribe<JointStateMsg>("/joint_states", UpdateJoints);
    }

    void UpdateJoints(JointStateMsg jointState)
    {
        // Loop through the received joint states
        for (int i = 0; i < jointState.name.Length; i++)
        {
            // Find the corresponding joint in the Unity model
            GameObject joint = GameObject.Find(jointState.name[i]);

            // Apply the rotation
            // This is a simplified example. You'll need to handle different
            // joint types and axes correctly.
            if (joint != null)
            {
                joint.transform.localRotation = Quaternion.Euler(0, jointState.position[i] * Mathf.Rad2Deg, 0);
            }
        }
    }
}
```

By following these steps, you can create a stunning digital twin of your robot that is animated in real-time by your ROS 2 simulation, giving you the best of both worlds: accurate physics and beautiful graphics.
