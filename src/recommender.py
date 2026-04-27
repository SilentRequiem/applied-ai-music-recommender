from typing import List, Dict, Tuple
from dataclasses import dataclass
from src.reliability import calculate_confidence
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        ranked = sorted(
            self.songs,
            key=lambda song: self._score_song(song, user)[0],
            reverse=True,
        )
        return ranked[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        _, reasons = self._score_song(song, user)
        return "; ".join(reasons)

    def _score_song(self, song: Song, user: UserProfile) -> Tuple[float, List[str]]:
        score = 0.0
        reasons: List[str] = []

        if song.genre == user.favorite_genre:
            score += 2.0
            reasons.append(f"genre matches your favorite ({user.favorite_genre})")

        if song.mood == user.favorite_mood:
            score += 1.5
            reasons.append(f"mood matches your favorite ({user.favorite_mood})")

        energy_bonus = max(0.0, 1.0 - abs(song.energy - user.target_energy))
        score += energy_bonus
        reasons.append(
            f"energy is close to your target ({song.energy:.2f} vs {user.target_energy:.2f})"
        )

        acoustic_match = user.likes_acoustic and song.acousticness >= 0.6
        acoustic_mismatch = not user.likes_acoustic and song.acousticness <= 0.4
        if acoustic_match or acoustic_mismatch:
            score += 0.75
            reasons.append("acousticness matches your preference")

        return score, reasons

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons: List[str] = []

    preferred_genres = user_prefs.get("genres") or [user_prefs.get("genre")]
    preferred_moods = user_prefs.get("moods") or [user_prefs.get("mood")]
    preferred_genres = [genre for genre in preferred_genres if genre]
    preferred_moods = [mood for mood in preferred_moods if mood]

    if song["genre"] in preferred_genres:
        score += user_prefs.get("genre_weight", 1.0)
        reasons.append(f"matches preferred genre {song['genre']}")

    if song["mood"] in preferred_moods:
        score += user_prefs.get("mood_weight", 1.5)
        reasons.append(f"matches preferred mood {song['mood']}")

    if "energy" in user_prefs:
        energy_bonus = max(0.0, 1.0 - abs(song["energy"] - user_prefs["energy"]))
        score += energy_bonus * user_prefs.get("energy_weight", 1.0)
        reasons.append(
            f"energy is close to target ({song['energy']:.2f} vs {user_prefs['energy']:.2f})"
        )

    if "tempo_bpm" in user_prefs:
        tempo_bonus = max(0.0, 1.0 - abs(song["tempo_bpm"] - user_prefs["tempo_bpm"]) / 80.0)
        score += tempo_bonus * user_prefs.get("tempo_weight", 0.75)
        reasons.append(
            f"tempo is close to target ({song['tempo_bpm']:.0f} vs {user_prefs['tempo_bpm']:.0f} BPM)"
        )

    if "acousticness" in user_prefs:
        acoustic_bonus = max(
            0.0,
            1.0 - abs(song["acousticness"] - user_prefs["acousticness"]),
        )
        score += acoustic_bonus * user_prefs.get("acousticness_weight", 0.75)
        reasons.append(
            "acousticness is close to your preference "
            f"({song['acousticness']:.2f} vs {user_prefs['acousticness']:.2f})"
        )

    if "valence" in user_prefs:
        valence_bonus = max(0.0, 1.0 - abs(song["valence"] - user_prefs["valence"]))
        score += valence_bonus * user_prefs.get("valence_weight", 0.5)
        reasons.append(
            f"emotional tone is close to target ({song['valence']:.2f} vs {user_prefs['valence']:.2f})"
        )

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs: List[Tuple[Dict, float, str, str]] = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)

        # NEW: calculate confidence
        confidence = calculate_confidence(score)

        # FIX: append result
        scored_songs.append((song, score, explanation, confidence))

    scored_songs.sort(key=lambda item: item[1], reverse=True)
    return scored_songs[:k]
