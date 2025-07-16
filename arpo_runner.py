# arpo_runner.py
# Simulate ARPO learning loop with fake rollout data

import os
import random

def simulate_episode(prompt):
    return 1 if "App List" in prompt else random.choice([0, 1])

def arpo_train(initial_prompt, iterations=5):
    current_prompt = initial_prompt
    rewards = []
    for i in range(iterations):
        reward = simulate_episode(current_prompt)
        rewards.append(reward)
        print(f"Episode {i+1}: Reward = {reward}")
        if reward == 0 and "App Icon" in current_prompt:
            current_prompt = current_prompt.replace("App Icon", "App List")
        elif reward == 0:
            current_prompt += " (precise)"
    print("Final Learned Prompt:", current_prompt)
    success_rate = sum(rewards) / len(rewards)
    print(f"Success Rate: {success_rate:.2%}")
    return current_prompt, rewards, success_rate

if __name__ == "__main__":
    base_prompt = 'CLICK("Slack App Icon")'
    final_prompt, rewards, rate = arpo_train(base_prompt)

    with open("results/arpo_log.txt", "w") as f:
        for i, r in enumerate(rewards, 1):
            f.write(f"Episode {i}: Reward = {r}\n")
        f.write(f"Final Learned Prompt: {final_prompt}\n")
        f.write(f"Success Rate: {rate:.2%}\n")
