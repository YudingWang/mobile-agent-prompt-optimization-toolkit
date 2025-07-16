# gemini_prompting.py
# Simulate prompt generation from a UI screenshot and goal

import os

def generate_prompt(goal, screen, options):
    prompt = f"Goal: {goal}\nCurrent screen: {screen}\nOptions: {options}\nAction: CLICK(\"{options[0]}\")"
    print(prompt)
    return prompt

if __name__ == "__main__":
    goal = "Uninstall Slack"
    screen = "Settings > Apps"
    options = ["Slack", "Permissions", "App Info"]
    prompt = generate_prompt(goal, screen, options)

    with open("results/gemini_log.txt", "w") as f:
        f.write(prompt + "\n")
