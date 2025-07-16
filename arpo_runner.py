import os
import random

def rollout(prompt: str) -> int:
    return 1 if "App List" in prompt else random.choice([0, 1])

def refine_prompt(prompt: str) -> str:
    if "App Icon" in prompt and "App List" not in prompt:
        return prompt.replace("App Icon", "App List")
    elif "AliExpress (confirmed)" not in prompt:
        return prompt.replace("AliExpress", "AliExpress (confirmed)")
    return prompt

def load_prompt_from_log(file_path):
    with open(file_path, "r") as f:
        for line in f:
            if line.startswith("Action: CLICK("):
                return line.strip().replace("Action: ", "")
    return 'CLICK("AliExpress")'

def train(prompt: str, episodes: int = 5):
    history = []
    for i in range(episodes):
        reward = rollout(prompt)
        history.append(reward)
        print(f"Episode {i+1}: Reward = {reward}")
        prompt = refine_prompt(prompt)

    success_rate = sum(history) / len(history)
    print(f"Final Learned Prompt: {prompt}")
    print(f"Success Rate: {success_rate:.2%}")

    os.makedirs("results", exist_ok=True)
    with open("results/arpo_log.txt", "w") as f:
        for i, r in enumerate(history, 1):
            f.write(f"Episode {i}: Reward = {r}\n")
        f.write(f"Final Learned Prompt: {prompt}\n")
        f.write(f"Success Rate: {success_rate:.2%}\n")

if __name__ == "__main__":
    initial_prompt = load_prompt_from_log("results/gemini_log.txt")
    train(initial_prompt)
