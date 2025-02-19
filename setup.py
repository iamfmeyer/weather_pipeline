from setuptools import setup, find_packages

setup(
    name="weather-pipeline",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "python-dotenv>=1.0.1",
        "pydantic>=2.6.1",
        "loguru>=0.7.2",
    ],
)
