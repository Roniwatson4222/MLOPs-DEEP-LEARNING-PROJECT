import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version = "0.0.0"

REPO_NAME = "MLOPs-Chest-Disease-Classification"
AUTHOR_USER_NAME = "satyarth"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "roniwatson42@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=setuptools.__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A machine learning project for classifying chest diseases using convolutional neural networks.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
)
