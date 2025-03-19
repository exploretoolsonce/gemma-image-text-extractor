"""Tests for the ImageProcessor class."""

import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path

from image_processor import ImageProcessor

class TestImageProcessor(unittest.TestCase):
    """Test cases for ImageProcessor class."""

    def setUp(self):
        """Set up test fixtures."""
        self.processor = ImageProcessor()
        self.test_image_path = "test_image.png"

    @patch('pathlib.Path.exists')
    @patch('ollama.chat')
    def test_process_image_success(self, mock_chat, mock_exists):
        """Test successful image processing."""
        # Mock the file existence check
        mock_exists.return_value = True

        # Mock the ollama chat response
        mock_response = {
            "message": {
                "content": "Test extracted text"
            }
        }
        mock_chat.return_value = mock_response

        # Process the image
        result = self.processor.process_image(self.test_image_path)

        # Verify the result
        self.assertEqual(result["text"], "Test extracted text")
        self.assertEqual(result["highlighted"], "")

        # Verify ollama.chat was called with correct parameters
        mock_chat.assert_called_once()
        call_args = mock_chat.call_args[1]
        self.assertEqual(call_args["model"], "gemma3:4b")
        self.assertEqual(len(call_args["messages"]), 1)
        self.assertEqual(call_args["messages"][0]["images"], [self.test_image_path])

    def test_process_image_not_found(self):
        """Test image processing with non-existent file."""
        with self.assertRaises(FileNotFoundError):
            self.processor.process_image("nonexistent.png")

if __name__ == '__main__':
    unittest.main() 