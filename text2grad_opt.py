# text2grad_opt.py
# Simulate prompt optimization using a fake reward function

import os

def reward_function(prompt):
    # Reward is based on whether the prompt uses more specific wording
    return 1.0 if "App Icon" in prompt else 0.6

def optimize_prompt(prompt):
    print("Original Prompt:", prompt)
    if "Slack" in prompt and "App Icon" not in prompt:
        optimized = prompt.replace("Slack", "Slack App Icon")
    else:
        optimized = prompt
    r1 = reward_function(prompt)
    r2 = reward_function(optimized)
    print("Optimized Prompt:", optimized)
    print(f"Reward improved from {r1} → {r2}")
    return prompt, optimized, r1, r2

if __name__ == "__main__":
    original_prompt = 'CLICK("Slack")'
    orig, opt, r1, r2 = optimize_prompt(original_prompt)

    with open("results/text2grad_log.txt", "w") as f:
        f.write(f"Original Prompt: {orig}\n")
        f.write(f"Optimized Prompt: {opt}\n")
        f.write(f"Reward improved from {r1} → {r2}\n")
