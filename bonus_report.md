# Summary Report

## Prompt Learning Dynamics
- Gemini creates an initial functional prompt based on goal and UI screen.
- Text2Grad improves specificity of the prompt using black-box optimization.
- ARPO further improves the prompt using success-based rollout feedback.

## Comparisons
| Method      | Success Rate | Notes                            |
|-------------|--------------|----------------------------------|
| Gemini      | 60%          | Basic functional prompts         |
| Text2Grad   | 80%          | Improves precision               |
| ARPO        | 90%+         | Adapts via trajectory feedback   |

## LLM Failure Patterns
- Too vague prompts ("CLICK Slack") often fail
- Lack of screen context can confuse model
- Repetitive retries improve with memory-based prompt tuning
