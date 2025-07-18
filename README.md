# Mobile Agent Prompt Optimization Toolkit

This toolkit provides a lightweight simulation framework for generating and optimizing prompts to control LLM-based agents in mobile UI environments (e.g., Android settings screens).

It combines prompt generation, gradient-based optimization, and reinforcement learning to progressively improve task success rates for mobile interface actions.

---

## Overview

The project consists of three core modules:

1. **Prompt Generation (`gemini_prompting.py`)**  
   Simulates structured prompt creation from visual UI context and task goals.

2. **Prompt Optimization (`text2grad_opt.py`)**  
   Refines the initial prompt using a black-box reward-based optimization method.

3. **Reinforcement Learning Loop (`arpo_runner.py`)**  
   Applies an episodic learning loop to update prompts based on task feedback and trajectory.

---

## Project Structure

| File | Description |
|------|-------------|
| `gemini_prompting.py` | Generates prompts from simulated Android UI states |
| `text2grad_opt.py` | Improves prompt wording via reward-driven edits |
| `arpo_runner.py` | Optimizes prompt using reinforcement learning signals |
| `prompt_optimization_report.md` | Experiment log and performance summary |
| `bonus_report.md` | Additional notes on prompt learning behavior |
| `results/` | Output logs from each module execution |

---

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/YudingWang/mobile-agent-prompt-optimization-toolkit.git
   cd mobile-agent-prompt-optimization-toolkit
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## How to Run

```bash
python gemini_prompting.py
python text2grad_opt.py
python arpo_runner.py
```

Each script writes logs into the `results/` folder.

---

## Sample Output

```
Episode 1: Reward = 0
Episode 2: Reward = 1
Episode 3: Reward = 1
Episode 4: Reward = 1
Episode 5: Reward = 1
Success Rate: 80.00%
Final Learned Prompt: CLICK("Slack App List")
```

