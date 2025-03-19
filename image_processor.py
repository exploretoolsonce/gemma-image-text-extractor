"""Module for processing images using the Gemma model through Ollama."""

import logging
from pathlib import Path
from typing import Dict, Any, Optional

import ollama
from config import MODEL_CONFIG, RESPONSE_FORMAT, LOG_CONFIG

# Configure logging
logging.basicConfig(**LOG_CONFIG)
logger = logging.getLogger(__name__)

class ImageProcessor:
    """Class for processing images and extracting text using the Gemma model."""

    def __init__(self, model_config: Optional[Dict[str, Any]] = None):
        """
        Initialize the ImageProcessor.

        Args:
            model_config: Optional configuration for the model. If None, uses default config.
        """
        self.model_config = model_config or MODEL_CONFIG
        self.response_format = RESPONSE_FORMAT

    def process_image(self, image_path: str) -> Dict[str, str]:
        """
        Process an image and extract text and highlighted content.

        Args:
            image_path: Path to the image file.

        Returns:
            Dictionary containing extracted text and highlighted text.

        Raises:
            FileNotFoundError: If the image file doesn't exist.
            ValueError: If the image processing fails.
        """
        if not Path(image_path).exists():
            raise FileNotFoundError(f"Image file not found: {image_path}")

        try:
            logger.info(f"Processing image: {image_path}")
            response = ollama.chat(
                model=self.model_config["model_name"],
                messages=[{
                    'role': 'user',
                    'content': 'Extract all the text from this image. and also give me which text is highlighted in white',
                    'images': [image_path]
                }]
            )
            
            # Process the response
            result = {
                "text": response.get("message", {}).get("content", ""),
                "highlighted": ""  # You might want to parse this from the response
            }
            
            logger.info("Successfully processed image")
            return result

        except Exception as e:
            logger.error(f"Error processing image: {str(e)}")
            raise ValueError(f"Failed to process image: {str(e)}")

def main():
    """Main function to demonstrate usage."""
    try:
        processor = ImageProcessor()
        result = processor.process_image('/home/ak/Downloads/check.png')
        print(f"Extracted text: {result['text']}")
        print(f"Highlighted text: {result['highlighted']}")
    except Exception as e:
        logger.error(f"Error in main: {str(e)}")
        raise

if __name__ == "__main__":
    main() 