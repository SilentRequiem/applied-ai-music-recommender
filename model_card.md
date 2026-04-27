# Model Card: Applied AI Music Recommender

## 1. Model Name

VibeMatch 2.0

---

## 2. System Overview

This system is a content-based music recommender that suggests songs based on a user’s preferences. It compares a user profile to song features and ranks songs based on similarity.

In this final version, the system also includes a **reliability component**, which assigns a confidence level (High, Medium, Low) to each recommendation and an evaluation script to test performance across multiple profiles.

---

## 3. Intended Use

This system is designed for learning and demonstration purposes. It shows how recommendation systems work using structured data and scoring logic.

It is not intended for real-world deployment or large-scale use, since it uses a small dataset and does not learn from user behavior.

---

## 4. Inputs

* User preferences:

  * genres (list)
  * moods (list)
  * energy
  * tempo_bpm
  * acousticness
  * valence
  * feature weights

* Song dataset:

  * title, artist
  * genre, mood
  * energy, tempo_bpm
  * acousticness, valence
  * danceability

---

## 5. Outputs

For each recommendation, the system returns:

* Song title
* Score (numerical match strength)
* Confidence level (High, Medium, Low)
* Explanation of why the song was recommended

---

## 6. How the Model Works

The system uses a weighted scoring approach.

* Genre match → highest impact
* Mood match → medium impact
* Numerical similarity (energy, tempo, acousticness, valence) → fine-tunes results

Each song is scored based on how close it is to the user profile. After scoring, songs are sorted and the top results are returned.

A reliability function then converts the score into a confidence level, helping interpret how strong the recommendation is.

---

## 7. Reliability Testing

The system includes an evaluation script that tests multiple user profiles.

Example test cases:

* High-energy pop
* Chill lofi
* Intense rock

Results showed:

* Correct top recommendations for each profile
* High confidence scores when features closely matched
* Lower confidence when profiles were less detailed

This confirms the system behaves consistently across different inputs.

---

## 8. Limitations and Biases

* The dataset is small, which limits diversity
* The system may over-prioritize genre due to weighting
* It does not learn from user behavior or feedback
* It simplifies music taste into numerical features

Because of this, recommendations may not reflect real-world listening patterns.

---

## 9. Misuse Risks

This system could be misused if treated as a fully accurate recommendation engine. Users might assume the results are complete or personalized, even though the system does not adapt or learn.

To prevent misuse:

* It should be clearly labeled as a simulation
* Users should understand its limitations

---

## 10. AI Collaboration Reflection

AI tools were used during development to help structure the system, debug issues, and improve design decisions.

One helpful example was generating ideas for adding a reliability system, which improved how results are interpreted.

One flawed example was initial suggestions that did not match the project structure or caused errors, which required manual correction.

This showed that AI is useful for support, but human review is still necessary to ensure correctness.

---

## 11. Future Work

* Expand dataset for better variety
* Improve feature weighting dynamically
* Add learning from user feedback
* Include more complex features like lyrics or listening patterns
* Improve confidence scoring with better evaluation metrics

---

## 12. Personal Reflection

This project showed how AI systems are not just about generating results, but also about evaluating and explaining them.

Adding reliability made the system feel more complete, because it now communicates not just what it recommends, but how confident it is.

It also showed how small changes in weights and features can significantly impact outputs, which highlights the importance of careful design in AI systems.
