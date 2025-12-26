# Quickstart Guide

**Date**: 2025-12-18

This guide provides instructions to set up the development environment for the project.

## 1. Prerequisites

-   **OS**: Ubuntu 22.04 LTS (Recommended for ROS 2)
-   **GPU**: NVIDIA GPU with >= 8GB VRAM (for Isaac Sim)
-   **Software**:
    -   Git
    -   Docker and Docker Compose
    -   Node.js (v18 or later)
    -   Python 3.11

## 2. Docusaurus Frontend Setup

1.  Clone the repository.
2.  Install dependencies: `npm install`
3.  Start the development server: `npm start`
4.  The site will be available at `http://localhost:3000`.

## 3. Chatbot API Setup

1.  Navigate to the `chatbot_api` directory.
2.  Create a virtual environment: `python3 -m venv venv`
3.  Activate the environment: `source venv/bin/activate`
4.  Install dependencies: `pip install -r requirements.txt`
5.  Run the API: `uvicorn src.main:app --reload`
6.  The API will be available at `http://localhost:8000`.

## 4. Robotics Simulation Setup

Detailed instructions for installing ROS 2, Gazebo, and NVIDIA Isaac Sim will be provided in Module 1, Chapter 1. This is a complex process and is documented within the book's content itself.
