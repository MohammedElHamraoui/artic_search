"""
API client for interacting with the Art Institute of Chicago API.
"""

import sys

import requests

from .config import API_URL, DEFAULT_LIMIT, FIELDS, HEADERS


def search_artworks(artist: str, limit: int = DEFAULT_LIMIT) -> list:
    """
    Fetches artworks from the Art Institute API based on the artist name.
    """
    params = {"q": artist, "limit": limit, "fields": FIELDS}
    response = requests.get(API_URL, params=params, headers=HEADERS)

    # Guard Clause: HTTP Errors
    if response.status_code != 200:
        print(
            f"Error: API request failed with status {response.status_code}.",
            file=sys.stderr,  # Much cleaner than __import__
        )
        return []

    return response.json().get("data", [])
