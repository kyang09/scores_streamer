import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scores",
    version="0.0.1",
    author="Kevin Yang",
    author_email="kevintoyang@gmail.com",
    description="Simple API for processing score data from a stream.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kyang09/scores_streamer", # Change to correct URL later.
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)