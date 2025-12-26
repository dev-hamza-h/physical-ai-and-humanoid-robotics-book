# Tasks: Physical AI Humanoid Robotics Book

**Input**: Design documents from `/specs/000-book-architecture/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Content files will be located in `docs/`.
- Module directories will be named `docs/module-<number>-<name>`.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure.

- [ ] T001 Set up Docusaurus frontend environment by following `specs/000-book-architecture/quickstart.md`.
- [ ] T002 Set up Chatbot API environment by following `specs/000-book-architecture/quickstart.md`.
- [X] T003 Create initial module directories: `docs/module-1-ros`, `docs/module-2-digital-twin`, `docs/module-3-ai-brain`, `docs/module-4-vla`.
- [X] T004 Create an `introduction.md` file in the `docs/` directory.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented.

- [X] T005 Configure Docusaurus sidebars in `sidebars.js` to include the introduction and all 4 modules.
- [X] T006 [P] Create a placeholder `_category_.json` file in `docs/module-1-ros` with a label "Module 1: The Robotic Nervous System".
- [X] T007 [P] Create a placeholder `_category_.json` file in `docs/module-2-digital-twin` with a label "Module 2: The Digital Twin".
- [X] T008 [P] Create a placeholder `_category_.json` file in `docs/module-3-ai-brain` with a label "Module 3: The AI-Robot Brain".
- [X] T009 [P] Create a placeholder `_category_.json` file in `docs/module-4-vla` with a label "Module 4: Vision-Language-Action".

---

## Phase 3: User Story 1 - Introduction (Priority: P1) 🎯 MVP

**Goal**: Write the book's introduction, setting the stage for the reader.
**Independent Test**: The `introduction.md` page renders correctly on the Docusaurus site with the specified content.

### Implementation for User Story 1
- [X] T010 [US1] Write the "Purpose" and "Target Audience" sections in `docs/introduction.md`.
- [X] T011 [US1] Write the "Overview of Modules" section, briefly describing each of the 4 modules in `docs/introduction.md`.
- [X] T012 [US1] Write the "Expected Outcomes" section, outlining what the reader will learn, in `docs/introduction.md`.

---

## Phase 4: User Story 2 - Module 1: The Robotic Nervous System (Priority: P2)

**Goal**: Detail the fundamentals of ROS 2 for robotics.
**Independent Test**: All three chapters for Module 1 render correctly and contain the required code examples and explanations.

### Implementation for User Story 2
- [X] T013 [P] [US2] Create file `docs/module-1-ros/chapter-1-ros-core.md`.
- [X] T014 [US2] Write content explaining ROS 2 Nodes, Topics, and Services with examples in `docs/module-1-ros/chapter-1-ros-core.md`.
- [X] T015 [US2] Add a tutorial for a simple publisher/subscriber in Python in `docs/module-1-ros/chapter-1-ros-core.md`.
- [X] T016 [P] [US2] Create file `docs/module-1-ros/chapter-2-rclpy-agents.md`.
- [X] T017 [US2] Write content on bridging Python agents to ROS controllers using `rclpy` in `docs/module-1-ros/chapter-2-rclpy-agents.md`.
- [X] T018 [US2] Include a code example of a Python agent controlling a ROS 2 action server in `docs/module-1-ros/chapter-2-rclpy-agents.md`.
- [X] T019 [P] [US2] Create file `docs/module-1-ros/chapter-3-urdf.md`.
- [X] T020 [US2] Explain the fundamentals of URDF for describing humanoid robots in `docs/module-1-ros/chapter-3-urdf.md`.
- [X] T021 [US2] Provide an example of a simple humanoid leg defined in URDF in `docs/module-1-ros/chapter-3-urdf.md`.

---

## Phase 5: User Story 3 - Module 2: The Digital Twin (Priority: P3)

**Goal**: Teach how to simulate humanoid robots in realistic environments.
**Independent Test**: All three chapters for Module 2 render correctly and describe the simulation setup.

### Implementation for User Story 3
- [X] T022 [P] [US3] Create file `docs/module-2-digital-twin/chapter-1-gazebo-physics.md`.
- [X] T023 [US3] Write content on simulating physics, gravity, and collisions in Gazebo for humanoids in `docs/module-2-digital-twin/chapter-1-gazebo-physics.md`.
- [X] T024 [US3] Provide a tutorial for setting up a Gazebo world with a simple ground plane and a robot model in `docs/module-2-digital-twin/chapter-1-gazebo-physics.md`.
- [X] T025 [P] [US3] Create file `docs/module-2-digital-twin/chapter-2-unity-rendering.md`.
- [X] T026 [US3] Write content on using Unity for high-fidelity rendering and human-robot interaction via a ROS bridge in `docs/module-2-digital-twin/chapter-2-unity-rendering.md`.
- [X] T027 [US3] Detail the steps to import a URDF into Unity and connect it to ROS 2 in `docs/module-2-digital-twin/chapter-2-unity-rendering.md`.
- [X] T028 [P] [US3] Create file `docs/module-2-digital-twin/chapter-3-sensor-simulation.md`.
- [X] T029 [US3] Explain how to simulate LiDAR, Depth Cameras, and IMUs in Gazebo or Unity in `docs/module-2-digital-twin/chapter-3-sensor-simulation.md`.
- [X] T030 [US3] Provide configuration examples for common sensors on a humanoid model in `docs/module-2-digital-twin/chapter-3-sensor-simulation.md`.

---

## Phase 6: User Story 4 - Module 3: The AI-Robot Brain (Priority: P4)

**Goal**: Cover AI techniques for robot perception and navigation.
**Independent Test**: All three chapters for Module 3 render correctly with explanations of the NVIDIA Isaac platform.

### Implementation for User Story 4
- [X] T031 [P] [US4] Create file `docs/module-3-ai-brain/chapter-1-isaac-sim.md`.
- [X] T032 [US4] Write a guide on using NVIDIA Isaac Sim for synthetic data generation in `docs/module-3-ai-brain/chapter-1-isaac-sim.md`.
- [X] T033 [US4] Include a tutorial for generating a dataset of images with ground truth labels in `docs/module-3-ai-brain/chapter-1-isaac-sim.md`.
- [X] T034 [P] [US4] Create file `docs/module-3-ai-brain/chapter-2-isaac-ros.md`.
- [X] T035 [US4] Write content on using Isaac ROS for VSLAM and navigation tasks in `docs/module-3-ai-brain/chapter-2-isaac-ros.md`.
- [X] T036 [US4] Provide an example of running Isaac ROS VSLAM on a simulated robot in `docs/module-3-ai-brain/chapter-2-isaac-ros.md`.
- [X] T037 [P] [US4] Create file `docs/module-3-ai-brain/chapter-3-nav2.md`.
- [X] T038 [US4] Explain how to use Nav2 for bipedal humanoid path planning, noting current challenges and approaches, in `docs/module-3-ai-brain/chapter-3-nav2.md`.
- [X] T039 [US4] Show a basic Nav2 setup for a humanoid-like robot in a simulated environment in `docs/module-3-ai-brain/chapter-3-nav2.md`.

---

## Phase 7: User Story 5 - Module 4: Vision-Language-Action (VLA) (Priority: P5)

**Goal**: Implement a voice-controlled robotics project.
**Independent Test**: All three chapters for Module 4 render correctly, culminating in a functional capstone project description.

### Implementation for User Story 5
- [X] T040 [P] [US5] Create file `docs/module-4-vla/chapter-1-voice-to-action.md`.
- [X] T041 [US5] Write content on building a voice-to-action pipeline with OpenAI Whisper in `docs/module-4-vla/chapter-1-voice-to-action.md`.
- [X] T042 [US5] Provide Python code for the FastAPI endpoint that transcribes audio using Whisper in `docs/module-4-vla/chapter-1-voice-to-action.md`.
- [X] T043 [P] [US5] Create file `docs/module-4-vla/chapter-2-cognitive-planning.md`.
- [X] T044 [US5] Explain how to use LLMs for cognitive planning to turn transcriptions into actionable robot commands in `docs/module-4-vla/chapter-2-cognitive-planning.md`.
- [X] T045 [US5] Show an example of a prompt and Python code for an LLM to generate a sequence of robot actions in `docs/module-4-vla/chapter-2-cognitive-planning.md`.
- [X] T046 [P] [US5] Create file `docs/module-4-vla/chapter-3-capstone-project.md`.
- [X] T047 [US5] Outline the capstone project: an autonomous humanoid that responds to voice commands in `docs/module-4-vla/chapter-3-capstone-project.md`.
- [X] T048 [US5] Provide the complete architecture and integration steps for the VLA pipeline in the capstone project in `docs/module-4-vla/chapter-3-capstone-project.md`.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories.

- [X] T049 [P] Review all chapters for technical accuracy and clarity.
- [X] T050 [P] Add citations in APA style to all chapters where external sources are referenced.
- [X] T051 Run a full build of the Docusaurus site to ensure no errors.
- [X] T052 Validate all code examples and tutorials for reproducibility.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Can start immediately.
- **Foundational (Phase 2)**: Depends on Setup completion. Blocks all user stories.
- **User Stories (Phase 3-7)**: Depend on Foundational phase completion. Can proceed in priority order or in parallel.
- **Polish (Phase 8)**: Depends on all user stories being complete.

### User Story Dependencies

- **US1 (Introduction)**: No dependencies on other stories.
- **US2-US5 (Modules 1-4)**: Can be developed in parallel after the Foundational phase is complete. There are conceptual dependencies (e.g., understanding ROS is a prerequisite for later modules), but the writing tasks themselves are parallelizable.

### Parallel Opportunities

- Most content creation tasks ([P] markers) can happen in parallel once the file structure is created. For instance, different authors could work on different chapters within the same module simultaneously.
- All module development (US2, US3, US4, US5) can occur in parallel.

---

## Implementation Strategy

### MVP First (User Story 1 & 2)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1 (Introduction)
4. Complete Phase 4: User Story 2 (Module 1)
5. **STOP and VALIDATE**: Deploy the site with the introduction and the first module. This provides the first valuable increment to readers.

### Incremental Delivery

1. Deliver MVP (Introduction + Module 1).
2. Add Module 2 → Deploy/Demo.
3. Add Module 3 → Deploy/Demo.
4. Add Module 4 → Deploy/Demo.
5. Each module adds a new, complete section to the book.
