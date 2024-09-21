import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shazamio",
    version="0.5.1",
    author="dotX12",
    description="Is a FREE asynchronous library from reverse engineered Shazam API written in Python 3.6+ with asyncio and aiohttp. Includes all the methods that Shazam has, including searching for a song by file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dotX12/ShazamIO",
    install_requires=[
        "aiohttp>=3.9.0,<4.0.0",
        "pydub",
        "numpy>=1.24.0,<2.0.0",
        "aiofiles>=23.2.1,<24.0.0",
        "dataclass-factory==2.16",
        "shazamio_core",
        "pydantic>=2.4.1,<2.10",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
)
