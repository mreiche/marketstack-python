from pathlib import Path

from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="marketstack",
    description="Inofficial Marketstack OpenAPI Python client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.4",
    url="https://github.com/mreiche/marketstack-python",
    author="Mike Reiche",
    py_modules=["marketstack"],
    install_requires=["attrs>=22.1.0", "httpx>=0.23.0", "python-dateutil>=2.8.2"],
    extra_test=[
        "pytest>=7.1.3",
    ],
)
