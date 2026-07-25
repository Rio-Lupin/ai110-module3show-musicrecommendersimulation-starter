# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**Prompts used:**

<!-- Paste the key prompts you gave the agent -->


**What did the agent generate or change?**

<!-- List the files edited, code generated, or commands run -->

**What did you verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Design Pattern (SF10)

> Document how AI helped you choose or implement a design pattern.

**Which design pattern did you use?**

<!-- e.g., Strategy, Factory, Observer, etc. -->
Deciding how to weigh the catagories.

Prompt
for the scoring logic design i think mood and energy whould weigh more than other catagories do you think this would be a good way to to score
**How did AI help you brainstorm or implement it?**

<!-- Describe the conversation or suggestions that led to your decision -->
Yes — that is a strong design choice, especially for this kind of music recommender.

Why it works:

Mood and energy are often the clearest signals of how a song “feels.”
They are more emotionally relevant than things like tempo or minor metadata.
For a user profile like “happy” and “high energy,” those two features should carry the most weight.
A good balance would be:

Mood: 0.35
Energy: 0.30
Genre: 0.20
Acousticness: 0.10
Tempo/valence: 0.05
That way:

mood and energy dominate the recommendation,
but genre still matters,
and the system does not become too narrow.
A simple rule could be:

give full points for exact mood match,
give strong points for being close to the target energy,
add smaller bonuses for genre preference and acoustic preference.
So my recommendation is: yes, make mood and energy the main drivers, but keep the other features as supporting signals rather than removing them entirely.

**How does the pattern appear in your final code?**

<!-- Point to the relevant class or method -->
