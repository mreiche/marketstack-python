from setuptools import setup

setup(
    name="marketstack",
    version="dev",
    url="https://github.com/mreiche/marketstack-python",
    author="Mike Reiche",
    py_modules=["marketstack"],
    install_requires=["attrs>=22.1.0", "httpx>=0.23.0", "python-dateutil>=2.8.2"],
    extra_test=[
        "pytest>=7.1.3",
    ],
)
