# Summary Report

## Prompt Learning Dynamics

- **Gemini** creates an initial prompt based on UI screenshot and task goal. Prompt quality can vary based on model wording.
- **Text2Grad** refines prompts using black-box optimization and reward evaluation (e.g., adding "App Icon").
- **ARPO** further improves prompt quality via reinforcement learning over multi-step simulated environments.

---

## Experimental Branches

We observed two types of Gemini output and evaluated how they affect the downstream optimization:

### Case 1: Gemini Returns Actionable Prompt
```
Gemini Output: Long-press the AliExpress app icon to uninstall.
Extracted Action: CLICK("AliExpress App Icon")
```

- Already scored **1.0** in reward function.
- **Text2Grad & ARPO not needed.**
- Success path with Gemini only.

### Case 2: Gemini Returns Vague Prompt
```
Gemini Output: The user should long-press the AliExpress icon...
Extracted Action: UNKNOWN
Fallback Action: CLICK("AliExpress")
```

- Text2Grad improved to `CLICK("AliExpress App Icon")` (score: 0.6 → 1.0).
- ARPO adapted to `CLICK("AliExpress (confirmed)")` and improved success rate to **80%**.

---

## Comparisons

| Method       | Success Rate | Notes                                      |
|--------------|--------------|--------------------------------------------|
| Gemini       | 60%~100%     | Quality depends on natural language style  |
| Text2Grad    | 80%          | Useful when Gemini outputs vague wording   |
| ARPO         | 90%+         | Best for multi-turn optimization           |

---

## LLM Failure Patterns

- Prompts like `CLICK("Slack")` often fail due to lack of UI specificity.
- Gemini sometimes outputs indirect phrases ("the user should...") that are hard to parse.
- Using stricter `extract_action()` with known UI targets improves reliability.
- Memory-based refinement and structured feedback loops (ARPO) improve generalization.

