# Applied AI Music Recommender

## Original Project

This project is based on my Module 3 Music Recommender Simulation. The original version focused on building a content-based recommender that scores songs based on how well they match a user’s preferences like genre, mood, and energy. It also generated explanations for why each song was recommended.

---

## Project Summary

This project extends the original recommender into a full applied AI system. It takes a user profile, compares it against a dataset of songs, ranks songs based on similarity, and now also evaluates the reliability of its own recommendations.

The system uses features like genre, mood, energy, tempo, acousticness, and valence to model a user’s taste and generate recommendations that match both category and overall vibe.

---

## AI Feature Added

The main AI feature added in this final version is a **reliability and evaluation system**.

Each recommendation now includes a confidence level (High, Medium, Low) based on how strong the match score is. This helps explain not just *what* the system recommends, but *how confident* it is in those recommendations.

An evaluation script was also added to test the system across multiple profiles and verify that the outputs are consistent and reasonable.

---

## Architecture Overview

The system follows this flow:

User Profile
↓
Song Dataset
↓
Scoring Engine
↓
Confidence / Reliability Checker
↓
Ranked Recommendations + Explanation
↓
Evaluation Script

---

## How to Run

### Run the recommender

```bash
python -m src.main
```

### Run evaluation tests

```bash
python -m evaluation.evaluate_profiles
```

---

## Sample Outputs

Example output from the system:

```
Sunrise City - Score: 6.51 - Confidence: High
Because: matches preferred genre pop; matches preferred mood happy; energy is close to target...
```

The system returns:

* Song title
* Score
* Confidence level
* Explanation

---

## Reliability and Evaluation

The system includes an evaluation script that runs multiple test profiles and checks the top recommendation for each case.

Example:

* Pop profile → Sunrise City (High confidence)
* Rock profile → Fire Within (High confidence)
* Lofi profile → Deep Focus (High confidence)

This shows that the system consistently returns results that match the intended genre and vibe.

---

## Design Decisions

I used a weighted scoring system instead of a strict rule-based system so the recommender could handle partial matches. This allows songs to rank well even if they are not perfect matches, which feels more realistic.

Genre and mood are treated as strong signals, while numerical features like energy, tempo, acousticness, and valence refine the results.

Adding confidence scoring was important because raw scores alone do not communicate how reliable a recommendation is.

---

## Limitations

* The dataset is small, so recommendations are limited
* The system does not learn from user behavior over time
* It may over-prioritize certain features depending on weights
* It does not consider lyrics, artists, or listening history

---

## Demo Video

(Add your Loom link here)

---

## Reflection

This project helped me understand how AI systems are built beyond just making predictions. Adding reliability and evaluation made me think more about whether the system is actually working, not just producing output.

One thing I noticed is how sensitive the system is to small changes. Adjusting weights or adding features can completely change the results. That showed me how important design decisions are in AI systems.

AI tools were helpful for speeding up development and suggesting structure, but I still had to verify the logic myself. Some suggestions worked well, but others needed adjustment to match the behavior I wanted.

Overall, this project shows how a simple system can simulate real recommendation systems at a smaller scale, while still dealing with issues like bias, reliability, and interpretation.
