# Chapter 2: Cognitive Planning with Large Language Models

Now that we have the transcribed text from Whisper, we need to understand its meaning and turn it into a command that our robot can execute. This is where Large Language Models (LLMs) come in.

## LLMs for Natural Language Understanding (NLU)

An LLM is a powerful tool for NLU. We can give it the transcribed text and ask it to perform several tasks:

*   **Intent Recognition**: What does the user want the robot to do? (e.g., "pick up an object," "move to a location").
*   **Entity Extraction**: What are the key objects or locations involved? (e.g., "the red cube," "the kitchen").
*   **Action Sequencing**: Break down a complex command into a sequence of simple actions that the robot can perform.

## In-Context Learning and Prompt Engineering

Instead of fine-tuning a custom model, we will use a technique called **in-context learning**. We will give the LLM a carefully crafted **prompt** that includes:

1.  **A high-level description** of its role (e.g., "You are a helpful robot assistant").
2.  **A list of the robot's available actions** (e.g., `PICK(object)`, `PLACE(location)`, `GOTO(location)`).
3.  **A few examples** of transcribed text and the corresponding desired robot action sequence (this is called "few-shot prompting").
4.  **The new transcription** that we want it to process.

The LLM will use the examples to "learn" how to transform the new transcription into a valid action sequence. This process of designing the perfect prompt is called **prompt engineering**.

## Creating a Cognitive Planning Service

We can create another FastAPI endpoint that takes the transcribed text, sends it to an LLM with our carefully crafted prompt, and returns the generated action sequence.

This service will be the "brain" of our VLA pipeline, translating the user's natural language commands into a structured plan that the robot's control system can understand and execute.

## Tutorial: LLM for Action Generation

Here is a Python example of how to use the OpenAI API to generate a robot action sequence from a transcribed text.

### 1. The Python Code

```python
import openai

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

def generate_action_plan(transcription: str) -> str:
    """
    Uses an LLM to generate a sequence of robot actions from a transcription.
    """
    prompt = f"""
You are a helpful robot assistant. You can control a robot with the following actions:
- PICK(object)
- PLACE(location)
- GOTO(location)

Translate the user's command into a sequence of actions.

---
User: "Pick up the red cube and put it on the blue table."
Actions:
PICK(red_cube)
PLACE(blue_table)
---
User: "Go to the kitchen."
Actions:
GOTO(kitchen)
---
User: "{transcription}"
Actions:
"""

    response = openai.Completion.create(
        engine="text-davinci-003",  # Or another powerful model
        prompt=prompt,
        max_tokens=100,
        temperature=0.1,
    )

    return response.choices[0].text.strip()


# Example usage
transcription = "Can you grab the apple from the counter?"
action_plan = generate_action_plan(transcription)
print(f"Transcription: {transcription}")
print(f"Action Plan: \n{action_plan}")

```

### 2. The Prompt Structure

The key to this code is the prompt.

*   **System Role**: "You are a helpful robot assistant."
*   **Action Space**: We define the specific actions the robot can take.
*   **Few-Shot Examples**: We provide two examples of a user command and the correct action sequence.
*   **The New Command**: We insert the new transcription and ask the model to generate the actions.

### 3. Running the Code

When you run this code, the `generate_action_plan` function will send the prompt to the OpenAI API. The LLM will analyze the prompt and, based on the examples, generate the action sequence for the new command.

For the example transcription "Can you grab the apple from the counter?", the output would be:

```
Transcription: Can you grab the apple from the counter?
Action Plan:
PICK(apple)
```

This generated plan can then be parsed and sent to the robot's action execution system, which would use the ROS 2 action servers we learned about in Module 1 to carry out the command.
