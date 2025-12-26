# Data Model: Book Content

**Date**: 2025-12-18

This document defines the data structures for the book's content.

## 1. Book

The root entity that contains all modules.

-   **`title`**: String (e.g., "Physical AI Humanoid Robotics Book")
-   **`version`**: String (e.g., "1.0.0")

## 2. Module

A top-level section of the book, representing a major topic area.

-   **`id`**: String (e.g., "001-ros")
-   **`title`**: String (e.g., "The Robotic Nervous System")
-   **`chapters`**: List<Chapter>

## 3. Chapter

A single content unit within a Module. Each chapter is a Markdown file.

-   **`id`**: String (e.g., "01-nodes-topics-services")
-   **`title`**: String (e.g., "ROS 2 Nodes, Topics, and Services")
-   **`path`**: String (file path to the Markdown file)
-   **`content`**: String (Markdown content)
