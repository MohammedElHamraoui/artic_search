"""
Display and presentation logic for search results.
"""

from .config import MIN_RELEVANCE_SCORE


def display_results(artworks: list, artist: str) -> None:
    """
        Evaluates the relevance of the artworks and prints them to the console.

    Args:
        artworks: List of artwork dictionaries from the API
        artist: The artist name that was searched for
    """

    # Guard Clause: Empty results
    if not artworks:
        print(f"No artworks found for '{artist}'.")
        return

    # Guard Clause: Relevance check (Elasticsearch fallback filter)
    top_score = artworks[0].get("_score", 0)
    if top_score < MIN_RELEVANCE_SCORE:
        print(f"No relevant artworks found for '{artist}'.")
        print("💡 Tip: Check your spelling (e.g., 'Van Gogh' instead of 'Vangogh').")
        return

    # Happy Path: Print the results
    print(f"\n🎨 Found relevant result(s) for '{artist}':\n")

    for art in artworks:
        title = art.get("title", "Unknown Title")
        artist_name = art.get("artist_display") or "Unknown Artist"
        date = art.get("date_display") or "Unknown Date"

        print(f"🖼️  {title}")
        print(f"   By: {artist_name}")
        print(f"   Date: {date}")
        print(f"   Score: {art['_score']:.2f}\n")
