# gemini_prompting.py (Gemini 2.5 Vision Version)

import google.generativeai as genai
import base64
from PIL import Image
import io

def load_image_bytes(image_path):
    with open(image_path, "rb") as img_file:
        return img_file.read()

def generate_prompt_from_image(image_path, task_goal):
    image_bytes = load_image_bytes(image_path)

    model = genai.GenerativeModel("gemini-pro-vision")
    response = model.generate_content([
        {"text": f"Goal: {task_goal}. Based on this screenshot, what should the user do next?"},
        {"image": image_bytes}
    ])

    result = response.text
    print("Generated Prompt:")
    print(result)
    return result

if __name__ == "__main__":
    import os

    # Replace with your actual API key
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    # Example usage
    task_goal = "Uninstall Slack"
    image_path = "screenshot.png"  # Provide your own screenshot
    generate_prompt_from_image(image_path, task_goal)
