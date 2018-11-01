import setuptools

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nightly",
    version="0.0.1",
    author="John E. Jones IV",
    author_email="johnj@casefoundation.org",
    description="Nightly is a simple utility for executing a command every evening.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johnjones4/nightly",
    packages=setuptools.find_packages(),
    scripts=["bin/nightly"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
