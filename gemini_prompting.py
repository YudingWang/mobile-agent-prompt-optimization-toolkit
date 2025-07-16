import os
import re
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

with open("screenshot.png", "rb") as f:
    image_data = f.read()

prompt = [
    {"text": "Goal: Uninstall AliExpress. Based on this screenshot, what should the user do next?"},
    {
        "inline_data": {
            "mime_type": "image/png",
            "data": image_data
        }
    }
]

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(prompt)

result_text = response.text.strip()
print("Gemini Output:")
print(result_text)

# Good Gemini Result
def extract_action(text):
    match = re.search(
        r'(?:tap|click|select|open|press(?: and hold)?|long-press).*?(?:on|the)?\s+(AliExpress(?: app)?(?: icon)?)',
        text,
        re.IGNORECASE
    )
    if match:
        obj = match.group(1).strip().title()
        return f'Action: CLICK("{obj}")'
    return "Action: UNKNOWN"

# # Bad Gemini Result
# def extract_action(text):
#     match = re.search(
#         r'(tap|click|select|open|press(?: and hold)?|long-press).*?(?:on|the)?\\s*([A-Z][a-zA-Z0-9\\s\\-]{1,40})',
#         text,
#         re.IGNORECASE
#     )
#     if match:
#         verb, obj = match.groups()
#         obj = re.split(r'\\s+(until|that|to|and)\\b', obj)[0].strip()
#         obj = obj.rstrip('.').title()
#         return f'Action: CLICK("{obj}")'
#     return "Action: UNKNOWN"


action_line = extract_action(result_text)
print(action_line)

os.makedirs("results", exist_ok=True)
with open("results/gemini_log.txt", "w") as f:
    f.write("Gemini Prompt Output:\n")
    f.write(result_text + "\n\n")
    f.write(action_line + "\n")
