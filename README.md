# Image Text Extraction with Gemma

This project uses the Gemma model through Ollama to extract text from images and identify highlighted text.

## Features

- Extract text from images
- Identify highlighted text in images
- Uses Gemma 3 4B model for processing

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Make sure you have Ollama installed and running on your system

## Usage

```python
from image_processor import ImageProcessor

# Initialize the processor
processor = ImageProcessor()

# Process an image
result = processor.process_image('path/to/your/image.png')
print(f"Extracted text: {result['text']}")
print(f"Highlighted text: {result['highlighted']}")
```

## Configuration

You can configure the model and other settings in `config.py`.

## License

MIT License 