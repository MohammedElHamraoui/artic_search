"""
Configuration and constants for the Art Institute API client.
"""

# API Configuration
API_URL = "https://api.artic.edu/api/v1/artworks/search"

# HTTP Headers
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0"
}

# Fields to request from the API
# We explicitly ask for _score so we can evaluate relevance later
FIELDS = "id,title,artist_display,date_display,_score"

# Search configuration
DEFAULT_LIMIT = 3
MIN_RELEVANCE_SCORE = 1.0
