# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.
 the Features used in each song in my system are genre,mood,energy,tempo_bpm,valence. The recomender computes the score my putting more weight on mood and enegy but also taking into consideration the other catagories. the app chooses songs based on the profile dictionary that represents the preference of the user.

 the agorithem recipe would be :
 Mood: 0.35
 Energy: 0.30
 Genre: 0.20
 Acousticness: 0.10
 Tempo/valence: 0.05

 some bias i might expect:
 Confirmation bias: if the system only rewards what the user already likes, it may keep recommending similar songs and reduce variety.
 User-profile bias: a profile based on one person’s taste may accidentally make the system seem universal or objective when it is really narrow.


---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

`Top recommendations:

1. Sunrise City
   Score: 1.00
   Reasons:
     - Mood matches the user's favorite mood.
     - Genre matches the user's favorite genre.
     - Energy is within the target range.
     - Acousticness fits the user's preference.
     - Positive valence adds a small bonus.
     - High danceability adds a small bonus.

2. Rooftop Lights
   Score: 0.92
   Reasons:
     - Mood matches the user's favorite mood.
     - Genre matches a preferred genre.
     - Energy is within the target range.
     - Acousticness fits the user's preference.
     - Positive valence adds a small bonus.
     - High danceability adds a small bonus.

3. Neon District
   Score: 0.70
   Reasons:
     - Mood matches a preferred mood.
     - Energy is within the target range.
     - Acousticness fits the user's preference.
     - Positive valence adds a small bonus.
     - High danceability adds a small bonus.

4. Gym Hero
   Score: 0.64
   Reasons:
     - Genre matches the user's favorite genre.
     - Energy is close to the target range.
     - Acousticness fits the user's preference.
     - Positive valence adds a small bonus.
     - High danceability adds a small bonus.

5. Night Drive Loop
   Score: 0.55
   Reasons:
     - Genre matches a preferred genre.
     - Energy is within the target range.
     - Acousticness fits the user's preference.
     - High danceability adds a small bonus.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



