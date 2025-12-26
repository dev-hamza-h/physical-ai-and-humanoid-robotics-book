# Research Findings for Book Architecture

**Date**: 2025-12-18

This document summarizes the research conducted to resolve the "NEEDS CLARIFICATION" items from the implementation plan.

## 1. Docusaurus Structure for Technical Book

-   **Decision**: Utilize Docusaurus's multi-instance docs feature. Each "Module" will be a separate docs plugin instance.
-   **Rationale**: This allows for independent sidebars and versioning per module, which is ideal for a complex, multi-part book. It keeps the navigation focused and scalable.
-   **Alternatives Considered**: A single docs instance with a deeply nested sidebar was rejected as it would become unwieldy as content grows.

## 2. Robotics Simulation Integration (ROS 2, Gazebo, Unity)

-   **Decision**: Use ROS 2 as the central middleware. Gazebo will be the primary physics simulator, while Unity will be used for high-fidelity rendering and advanced HRI scenarios via the ROS-Unity bridge.
-   **Rationale**: This hybrid approach leverages the strengths of each tool. Gazebo provides robust and widely-supported physics simulation for robotics, while Unity offers superior graphics and a rich environment for creating interactive digital twins. ROS 2 ensures seamless communication between all components.
-   **Alternatives Considered**: Using only Gazebo (simpler setup, but limited rendering quality) or only Unity (more complex to set up for accurate physics from scratch).

## 3. VLA Pipeline (Whisper + LLM + ROS 2)

-   **Decision**: Implement a FastAPI backend that exposes an endpoint to receive audio data. The backend will use OpenAI's Whisper for transcription, an LLM (e.g., from OpenAI or a local model) for cognitive planning (intent recognition and task generation), and `rclpy` to publish commands to a ROS 2 action server.
-   **Rationale**: This architecture decouples the voice interface from the robot's control system, promoting modularity. FastAPI is a lightweight and high-performance choice for the API.
-   **Alternatives Considered**: A single, monolithic ROS 2 node was rejected as it would be harder to maintain and test.

## 4. RAG Chatbot Implementation

-   **Decision**: Use `sentence-transformers` to generate embeddings for each Markdown chapter. The embeddings and content will be stored in ChromaDB. A FastAPI endpoint will take a user query, generate an embedding, query ChromaDB for relevant context, and pass the context and query to an LLM to generate an answer.
-   **Rationale**: This is a standard and effective RAG architecture. ChromaDB is lightweight and easy to integrate.
-   **Alternatives Considered**: Using a cloud-based vector database service, which would increase cost and complexity for this project's scale.

## 5. Performance Goals and Constraints

-   **Performance Goals**:
    -   **Chatbot**: p95 response time < 3 seconds.
    -   **Simulations**: Real-Time Factor (RTF) >= 0.7 for all standard simulation tasks.
-   **Constraints**:
    -   **Hardware**: Simulations will require a Linux machine with a dedicated NVIDIA GPU (for Isaac Sim and high-fidelity rendering). Minimum specs will be detailed in the `quickstart.md`.
