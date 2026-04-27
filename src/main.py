"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from typing import Dict

from src.recommender import load_songs, recommend_songs


SAMPLE_USER_PROFILE: Dict = {
    "genre": "pop",
    "mood": "happy",
    "energy": 0.82,
}

HIGH_ENERGY_POP: Dict = {
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
}

CHILL_LOFI: Dict = {
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
}

INTENSE_ROCK: Dict = {
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
}


def print_profile_review() -> None:
    intense_rock = {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.91,
        "tempo_bpm": 152,
        "acousticness": 0.10,
    }
    chill_lofi = {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.35,
        "tempo_bpm": 72,
        "acousticness": 0.86,
    }

    print("Sample user profile:")
    print(SAMPLE_USER_PROFILE)
    print()
    print("Evaluation:")
    print(
        "This profile clearly leans toward upbeat pop because it asks for pop, happy mood, "
        "and high energy."
    )
    print(
        "It can separate intense rock from chill lofi mainly through energy: intense rock is "
        "closer on energy, while chill lofi is far away on both mood and energy."
    )
    print(
        "But it is still too narrow because it ignores tempo and acousticness, so it cannot "
        "explain whether the user prefers polished dance-pop, aggressive rock, or mellow electronic pop."
    )
    print()
    print("Contrast examples:")
    print(f"Intense rock example: {intense_rock}")
    print(f"Chill lofi example:  {chill_lofi}")
    print()
    print("Improved user profile:")
    print(HIGH_ENERGY_POP)
    print()
    print("Why this helps:")
    print(
        "The improved version keeps the main taste signal but adds tempo, acousticness, and valence, "
        "which makes the profile more specific without reducing the user to just one genre and one mood."
    )
    print(
        "Using lists for genres and moods also captures adjacent styles a real listener might enjoy, "
        "so the recommender can prefer upbeat pop and synthy tracks while still rejecting chill lofi "
        "and intense rock when other features do not fit."
    )
    print()


def print_recommendations(label: str, profile: dict, songs: list) -> None:
    print(f"\n=== {label} ===\n")
    recommendations = recommend_songs(profile, songs, k=5)

    for song, score, explanation, confidence in recommendations:
        print(f"{song['title']} - Score: {score:.2f} - Confidence: {confidence}")
        print(f"Because: {explanation}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Total songs loaded: {len(songs)}")

    print_recommendations("High-Energy Pop", HIGH_ENERGY_POP, songs)
    print_recommendations("Chill Lofi", CHILL_LOFI, songs)
    print_recommendations("Intense Rock", INTENSE_ROCK, songs)


if __name__ == "__main__":
    main()
