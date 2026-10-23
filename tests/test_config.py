"""Tests for the configuration module."""

from artic_search.config import API_URL, MIN_RELEVANCE_SCORE


def test_api_url_is_set() -> None:
    assert API_URL == "https://api.artic.edu/api/v1/artworks/search"


def test_min_relevance_score() -> None:
    assert MIN_RELEVANCE_SCORE == 1.0
