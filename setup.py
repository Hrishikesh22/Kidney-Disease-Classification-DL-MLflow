import setuptools

REPO_NAME = "Kidney-Disease-Classification-DL-MLflow"
AUTHOR_USER_NAME = "Hrishikesh22"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "hrishikeshgokhale13@gmail.com"

__version__ = "0.0.0"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)