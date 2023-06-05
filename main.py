import os
import subprocess
from fastapi import FastAPI
import requests

app = FastAPI()

@app.post("/process_prompt")
async def process_prompt(prompt: str, output_filename: str, output_dir: str):
    bark_command = f"python -m bark --text \"{prompt}\" --output_filename \"{output_filename}\" --output_dir \"{output_dir}\""

    # Run the Bark command
    try:
        subprocess.check_output(bark_command, shell=True)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

    # Return the result
    return {"message": "Prompt processed successfully."}

@app.get("/")
async def root():
    return {"message": "Welcome to the Bark API!"}
