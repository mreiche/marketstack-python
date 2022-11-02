from setuptools import setup

setup(
    name="marketstack",
    version="0.1",
    url="https://github.com/mreiche/marketstack",
    author="Mike Reiche",
    author_email="mike@reiche.world",
    py_modules=["marketstack"],
    install_requires=[],
    extra_test=[
        "pytest>=7.1.3",
    ],
)
