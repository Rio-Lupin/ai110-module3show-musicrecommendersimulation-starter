import csv
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

DEFAULT_TASTE_PROFILE: Dict[str, object] = {
    "favorite_genre": "pop",
    "preferred_genres": ["pop", "indie pop", "synthwave"],
    "favorite_mood": "happy",
    "preferred_moods": ["happy", "energetic", "upbeat"],
    "target_energy": 0.75,
    "energy_range": (0.65, 0.9),
    "likes_acoustic": False,
}


def build_sample_user_profiles() -> List[Dict[str, object]]:
    """Return a set of example user preference dictionaries for evaluation."""
    return [
        {
            "name": "High-Energy Pop",
            "favorite_genre": "pop",
            "preferred_genres": ["pop", "dance-pop", "synthwave"],
            "favorite_mood": "happy",
            "preferred_moods": ["happy", "energetic", "upbeat"],
            "target_energy": 0.8,
            "energy_range": (0.7, 0.95),
            "likes_acoustic": False,
        },
        {
            "name": "Chill Lofi",
            "favorite_genre": "lofi",
            "preferred_genres": ["lofi", "ambient", "jazz"],
            "favorite_mood": "chill",
            "preferred_moods": ["chill", "calm", "reflective"],
            "target_energy": 0.3,
            "energy_range": (0.15, 0.45),
            "likes_acoustic": True,
        },
        {
            "name": "Deep Intense Rock",
            "favorite_genre": "rock",
            "preferred_genres": ["rock", "alternative", "metal"],
            "favorite_mood": "intense",
            "preferred_moods": ["intense", "dramatic", "dark"],
            "target_energy": 0.85,
            "energy_range": (0.75, 0.95),
            "likes_acoustic": False,
        },
        {
            "name": "Adversarial Conflicted",
            "favorite_genre": "pop",
            "preferred_genres": ["pop", "ambient", "rock"],
            "favorite_mood": "sad",
            "preferred_moods": ["sad", "melancholic", "energetic"],
            "target_energy": 0.9,
            "energy_range": (0.85, 0.95),
            "likes_acoustic": False,
        },
    ]


def evaluate_profiles(songs: List[Dict], profiles: Optional[List[Dict[str, object]]] = None) -> List[Tuple[str, List[Tuple[Dict, float, str]]]]:
    """Return top recommendations for each profile for system evaluation."""
    if profiles is None:
        profiles = build_sample_user_profiles()

    results: List[Tuple[str, List[Tuple[Dict, float, str]]]] = []
    for profile in profiles:
        name = str(profile.get("name", "Unnamed Profile"))
        recommendations = recommend_songs(profile, songs, k=3)
        results.append((name, recommendations))
    return results

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
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of dictionaries."""
    path = Path(csv_path)
    if not path.is_absolute():
        base_dir = Path(__file__).resolve().parent.parent
        path = base_dir / path

    with path.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        songs: List[Dict] = []
        for row in reader:
            song: Dict[str, object] = {}
            for key, value in row.items():
                if key in {"id", "tempo_bpm"}:
                    song[key] = int(value)
                elif key in {"energy", "valence", "danceability", "acousticness"}:
                    song[key] = float(value)
                else:
                    song[key] = value
            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against a user's taste profile and return a numeric score with reasons."""
    score = 0.0
    reasons: List[str] = []

    preferred_genres = user_prefs.get("preferred_genres", [])
    preferred_moods = user_prefs.get("preferred_moods", [])
    favorite_genre = user_prefs.get("favorite_genre")
    favorite_mood = user_prefs.get("favorite_mood")
    target_energy = user_prefs.get("target_energy", 0.0)
    energy_range = user_prefs.get("energy_range", (0.0, 1.0))
    likes_acoustic = user_prefs.get("likes_acoustic", False)

    genre = song.get("genre", "")
    mood = song.get("mood", "")
    energy = float(song.get("energy", 0.0))
    acousticness = float(song.get("acousticness", 0.0))
    valence = float(song.get("valence", 0.0))
    danceability = float(song.get("danceability", 0.0))

    if favorite_mood and mood == favorite_mood:
        score += 0.35
        reasons.append("Mood matches the user's favorite mood.")
    elif preferred_moods and mood in preferred_moods:
        score += 0.25
        reasons.append("Mood matches a preferred mood.")

    if favorite_genre and genre == favorite_genre:
        score += 0.20
        reasons.append("Genre matches the user's favorite genre.")
    elif preferred_genres and genre in preferred_genres:
        score += 0.12
        reasons.append("Genre matches a preferred genre.")

    if energy_range:
        min_energy, max_energy = energy_range
        if min_energy <= energy <= max_energy:
            score += 0.30
            reasons.append("Energy is within the target range.")
        else:
            distance = min(abs(energy - min_energy), abs(energy - max_energy))
            score += max(0.0, 0.30 - distance * 0.4)
            reasons.append("Energy is close to the target range.")
    else:
        energy_gap = abs(energy - target_energy)
        score += max(0.0, 0.30 - energy_gap * 0.4)
        reasons.append("Energy is close to the target energy.")

    if likes_acoustic is False and acousticness <= 0.5:
        score += 0.10
        reasons.append("Acousticness fits the user's preference.")
    elif likes_acoustic is True and acousticness > 0.5:
        score += 0.10
        reasons.append("Acousticness fits the user's preference.")

    if valence > 0.6:
        score += 0.025
        reasons.append("Positive valence adds a small bonus.")
    if danceability > 0.6:
        score += 0.025
        reasons.append("High danceability adds a small bonus.")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs by score and return the top k recommendations for a user."""
    scored_songs = [
        (song, score, "; ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]
    scored_songs.sort(key=lambda item: item[1], reverse=True)
    return scored_songs[:k]
