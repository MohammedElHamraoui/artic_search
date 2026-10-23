"""Tests for the API client."""

from unittest.mock import MagicMock, patch

from artic_search.client import search_artworks


@patch("artic_search.client.requests.get")
def test_search_artworks_success(mock_get: MagicMock) -> None:
    """Test successful API response."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"data": [{"title": "Water Lilies", "_score": 100}]}
    mock_get.return_value = mock_response

    result = search_artworks("Monet")

    assert len(result) == 1
    assert result[0]["title"] == "Water Lilies"
    mock_get.assert_called_once()


@patch("artic_search.client.requests.get")
def test_search_artworks_http_error(mock_get: MagicMock, capsys: object) -> None:
    """Test API failure returns empty list and prints error."""
    mock_response = MagicMock()
    mock_response.status_code = 403
    mock_get.return_value = mock_response

    result = search_artworks("Monet")

    assert result == []
    captured = capsys.readouterr()  # type: ignore[attr-defined]
    assert "Error: API request failed with status 403" in captured.err
