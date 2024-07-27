from setuptools import setup, find_packages

__version__ = "0.0.0"
REPO_NAME = "US-Visa-Approval"
AUTHOR_USER_NAME = "thinkingdatascience"
AUTHOR_EMAIL = "thinkingdatascience@gmail.com"

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for ML-Classification",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    packages=find_packages(),
)
