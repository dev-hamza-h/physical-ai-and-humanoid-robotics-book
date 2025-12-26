# Implementation Plan: Book Architecture and Workflow

**Branch**: `000-book-architecture` | **Date**: 2025-12-18 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/000-book-architecture/spec.md`

## Summary

This plan outlines the architecture for the "Physical AI Humanoid Robotics Book," a Docusaurus-based project. It integrates a RAG chatbot using FastAPI and ChromaDB, and defines the structure for robotics simulation modules with ROS 2, Gazebo, and Unity. The development will follow a Spec-Driven Development (SDD) methodology.

## Technical Context

**Language/Version**: JavaScript (Docusaurus/React), Python 3.11 (FastAPI, rclpy)
**Primary Dependencies**: Docusaurus, React, FastAPI, Uvicorn, ChromaDB, sentence-transformers, ROS 2, Gazebo, Unity, NVIDIA Isaac, OpenAI Whisper
**Storage**: ChromaDB for RAG embeddings; Markdown files for book content.
**Testing**: Jest for frontend; pytest for backend API.
**Target Platform**: Docusaurus site on GitHub Pages; Robotics simulations on Linux (with ROS 2).
**Project Type**: Web application (Docusaurus frontend, FastAPI backend) with integrated robotics simulation components.
**Performance Goals**: Chatbot response time p95 < 3s; Simulation Real-Time Factor (RTF) >= 0.7. See `research.md` for details.
**Constraints**: Requires a Linux machine with a dedicated NVIDIA GPU for simulations. See `research.md` and `quickstart.md` for details.
**Scale/Scope**: The book will consist of 4 core modules, each with multiple chapters.

## Constitution Check

*GATE: Must pass before proceeding. Re-check after design.*

- [x] **Clarity & Accessibility**: Is the feature's purpose and design clear? Is it accessible to the target audience?
- [x] **Practical Application**: Does this feature solve a real-world problem for the user? Is it grounded in a practical use case?
- [x] **Rigorous Accuracy**: Have technical claims, data, and algorithms been verified? Is there a plan for testing accuracy?
- [x] **Visual Learning**: If the feature involves complex information, are there plans for diagrams, charts, or other visual aids?
- [x] **Open Source**: If the feature includes code, does it adhere to the project's open-source licensing?
- [x] **Community Driven**: Is there a clear path for community feedback on this feature?

## Project Structure

### Documentation (this feature)

```text
specs/000-book-architecture/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/
│   └── vla-api.v1.yaml  # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
# Web Application Structure
chatbot_api/
├── src/
│   ├── core/
│   ├── models/
│   └── main.py
└── tests/

src/
├── components/
├── pages/
└── css/

# Content & Simulation Structure
docs/
├── module-1-intro/
└── module-2-ros/

# (Additional simulation directories to be created as needed)
```

**Structure Decision**: The project is a hybrid system. The Docusaurus site (`src/`, `docs/`) and the FastAPI backend (`chatbot_api/`) follow a standard web application structure. The core book content resides in `docs/`. Robotics simulation code will be organized within dedicated directories corresponding to the book modules as they are developed.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| *No violations detected* | N/A        | N/A                                 |
