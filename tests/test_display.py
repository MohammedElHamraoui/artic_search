"""Tests for the display logic."""

from artic_search.display import display_results


def test_display_empty_list(capsys: object) -> None:
    """Test output when no artworks are found."""
    display_results([], "Picasso")
    captured = capsys.readouterr()  # type: ignore[attr-defined]
    assert "No artworks found for 'Picasso'" in captured.out


def test_display_low_relevance(capsys: object) -> None:
    """Test output when Elasticsearch returns fallback garbage."""
    artworks = [{"title": "Self-Portrait", "_score": 0.0001}]
    display_results(artworks, "XyZ")
    captured = capsys.readouterr()  # type: ignore[attr-defined]
    assert "No relevant artworks found" in captured.out


def test_display_happy_path(capsys: object) -> None:
    """Test output when valid artworks are found."""
    artworks = [
        {
            "title": "The Bedroom",
            "artist_display": "Vincent van Gogh",
            "date_display": "1889",
            "_score": 3454.84,
        }
    ]
    display_results(artworks, "Van Gogh")
    captured = capsys.readouterr()  # type: ignore[attr-defined]
    assert "The Bedroom" in captured.out
    assert "Vincent van Gogh" in captured.out
