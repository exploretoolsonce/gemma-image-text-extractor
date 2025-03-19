"""Setup file for the package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="gemma-image-text-extractor",
    version="0.1.0",
    author="exploretoolsonce",
    author_email="your.email@example.com",  # Update this
    description="A Python package that uses Gemma model through Ollama to extract text from images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/exploretoolsonce/gemma-image-text-extractor",
    packages=find_packages(exclude=["tests*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    test_suite="tests",
) 