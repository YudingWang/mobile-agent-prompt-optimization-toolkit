import os

def reward_function(prompt: str) -> float:
    if "App Icon" in prompt:
        return 1.0
    elif "AliExpress" in prompt:
        return 0.6
    else:
        return 0.3

def optimize_prompt(prompt: str) -> str:
    if "App Icon" not in prompt and "AliExpress" in prompt:
        return prompt.replace("AliExpress", "AliExpress App Icon")
    return prompt

def load_prompt_from_log(file_path):
    with open(file_path, "r") as f:
        for line in f:
            if line.startswith("Action: CLICK("):
                return line.strip().replace("Action: ", "")
    return 'CLICK("AliExpress")'

def main():
    prompt = load_prompt_from_log("results/gemini_log.txt")
    optimized_prompt = optimize_prompt(prompt)
    reward_before = reward_function(prompt)
    reward_after = reward_function(optimized_prompt)

    print(f"Original Prompt: {prompt}")
    print(f"Optimized Prompt: {optimized_prompt}")
    print(f"Reward improved from {reward_before} → {reward_after}")

    os.makedirs("results", exist_ok=True)
    with open("results/text2grad_log.txt", "w") as f:
        f.write(f"Original Prompt: {prompt}\n")
        f.write(f"Optimized Prompt: {optimized_prompt}\n")
        f.write(f"Reward improved from {reward_before} → {reward_after}\n")

if __name__ == "__main__":
    main()
