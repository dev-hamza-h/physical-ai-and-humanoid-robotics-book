# Chapter 1: Building a Voice-to-Action Pipeline

Welcome to the final and most exciting module: Vision-Language-Action (VLA). In this module, we'll build a system that allows you to control your robot using natural language voice commands.

## The VLA Pipeline

A VLA pipeline is a series of steps that transform a spoken command into a robot action. Our pipeline will look like this:

1.  **Audio Input**: The user speaks a command into a microphone.
2.  **Speech-to-Text**: We use a speech-to-text engine to transcribe the audio into text.
3.  **Natural Language Understanding (NLU)**: An AI model (in our case, a Large Language Model) interprets the text to understand the user's intent and extracts key information.
4.  **Action Generation**: The NLU output is used to generate a specific robot action (e.g., "pick up the red cube").
5.  **Action Execution**: The generated action is sent to the robot's control system for execution.

## Speech-to-Text with OpenAI Whisper

For the speech-to-text component, we will use **OpenAI's Whisper**. Whisper is a state-of-the-art speech recognition model that is known for its high accuracy and robustness to background noise.

We will create a simple web API using FastAPI that accepts an audio file and returns the transcribed text. This API will serve as the entry point to our VLA pipeline.

Why use an API?

*   **Modularity**: The speech recognition service is decoupled from the rest of the system.
*   **Flexibility**: We can easily swap out Whisper for another speech-to-text engine in the future without changing the rest of our pipeline.
*   **Scalability**: The API can be deployed on a separate server if needed to handle a high volume of requests.

## Tutorial: FastAPI Endpoint for Whisper

Here is the Python code for a simple FastAPI server that takes an audio file and uses the `whisper` library to transcribe it.

### 1. Installation

First, you'll need to install the necessary libraries:

```bash
pip install fastapi uvicorn python-multipart openai-whisper
```

### 2. The FastAPI Code (`main.py`)

```python
import whisper
from fastapi import FastAPI, UploadFile, File

app = FastAPI()

# Load the Whisper model
# "base" is a good starting point. Other options include "tiny", "small", "medium", "large"
model = whisper.load_model("base") 

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    """
    Transcribes an audio file using OpenAI's Whisper model.
    """
    # Save the uploaded file temporarily
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())

    # Transcribe the audio file
    result = model.transcribe(file.filename)
    transcription = result["text"]

    return {"transcription": transcription}

# To run the server:
# uvicorn main:app --reload
```

### 3. How to Use It

1.  **Run the server**: `uvicorn main:app --reload`
2.  **Send an audio file**: You can use a tool like `curl` or a simple Python script to send a `POST` request to the `/transcribe` endpoint with your audio file.

**Example using `curl`:**

```bash
curl -X POST -F "file=@/path/to/your/audio.wav" http://localhost:8000/transcribe
```

The server will respond with a JSON object containing the transcription:

```json
{"transcription": "Hello, this is a test."}
```

This simple API is the first step in our VLA pipeline. In the next chapter, we'll take this transcribed text and use a Large Language Model to understand its meaning.
