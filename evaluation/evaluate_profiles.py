from src.recommender import load_songs, recommend_songs

songs = load_songs("data/songs.csv")

test_profiles = [
    {
        "genres": ["pop", "indie pop", "synthwave"],
        "moods": ["happy", "excited", "moody"],
        "energy": 0.78,
        "tempo_bpm": 118,
        "acousticness": 0.22,
        "valence": 0.74,
        "genre_weight": 2.0,
        "mood_weight": 1.25,
        "tempo_weight": 0.9,
        "acousticness_weight": 0.8,
        "valence_weight": 0.7,
    },
    {
        "genres": ["rock", "edm", "hiphop"],
        "moods": ["intense", "confident", "excited"],
        "energy": 0.90,
        "tempo_bpm": 135,
        "acousticness": 0.12,
        "valence": 0.55,
        "genre_weight": 2.0,
        "mood_weight": 1.25,
        "tempo_weight": 0.9,
        "acousticness_weight": 0.8,
        "valence_weight": 0.7,
    },
    {
        "genres": ["lofi", "ambient", "jazz"],
        "moods": ["chill", "calm", "focused", "relaxed"],
        "energy": 0.28,
        "tempo_bpm": 72,
        "acousticness": 0.82,
        "valence": 0.60,
        "genre_weight": 2.0,
        "mood_weight": 1.25,
        "tempo_weight": 0.9,
        "acousticness_weight": 0.8,
        "valence_weight": 0.7,
    },
]

print("=== Evaluation Results ===\n")

for i, profile in enumerate(test_profiles):
    print(f"Test Case {i + 1}: {profile}")

    results = recommend_songs(profile, songs)
    top_song, score, explanation, confidence = results[0]

    print(f"Top Song: {top_song['title']}")
    print(f"Score: {score:.2f}")
    print(f"Confidence: {confidence}")
    print(f"Reason: {explanation}")
    print()