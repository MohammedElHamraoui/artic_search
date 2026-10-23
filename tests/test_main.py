"""Tests for the main entry point."""

from unittest.mock import MagicMock, patch

from artic_search.main import main


@patch("artic_search.main.display_results")
@patch("artic_search.main.search_artworks")
@patch("builtins.input", return_value="Monet")
def test_main_calls_functions(
    mock_input: MagicMock, mock_search: MagicMock, mock_display: MagicMock
) -> None:
    """Test that main() orchestrates the search and display correctly."""
    # Now Pylance knows mock_search is a MagicMock and has return_value
    mock_search.return_value = [{"title": "Water Lilies"}]

    main()

    # Now Pylance knows these are Mock assertions
    mock_search.assert_called_once_with("Monet")
    mock_display.assert_called_once_with([{"title": "Water Lilies"}], "Monet")
