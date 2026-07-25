"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from .recommender import DEFAULT_TASTE_PROFILE, load_songs, recommend_songs
except ImportError:  # pragma: no cover - allows running file directly
    from recommender import DEFAULT_TASTE_PROFILE, load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Specific taste profile used for comparisons
    user_prefs = DEFAULT_TASTE_PROFILE

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for index, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        print(f"{index}. {song['title']}")
        print(f"   Score: {score:.2f}")
        print("   Reasons:")
        for reason in explanation.split("; "):
            print(f"     - {reason}")
        print()


if __name__ == "__main__":
    main()
