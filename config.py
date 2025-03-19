"""Configuration settings for the image processing application."""

from typing import Dict, Any

# Model configuration
MODEL_CONFIG: Dict[str, Any] = {
    "model_name": "gemma3:4b",
    "temperature": 0.7,
    "max_tokens": 1000,
}

# Response format
RESPONSE_FORMAT = {
    "type": "object",
    "properties": {
        "text": {
            "type": "string"
        },
        "highlighted": {
            "type": "string"
        }
    },
}

# Logging configuration
LOG_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "filename": "app.log"
} 