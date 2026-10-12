from pathlib import Path

from setuptools import find_packages, setup

requirements = [
    line.strip()
    for line in Path("requirements.txt").read_text(encoding="utf-8").splitlines()
    if line.strip() and not line.startswith("#")
]

setup(
    name="medical_chatbot",
    version="0.1.0",
    author="sakshi",
    author_email="sakshiarun2005singh@gmail.com",
    packages=find_packages(),
    install_requires=requirements,
)