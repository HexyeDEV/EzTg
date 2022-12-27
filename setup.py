import setuptools

with open("./README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EzTg",
    version="0.2.0",
    author="Hexye",
    author_email="dragonsale22@gmail.com",
    description="An api wrapper for telegram easy to use according to telegram core.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HexyeDEV/EzTg/",
    download_url="https://github.com/HexyeDEV/EzTg/releases",
    project_urls={
        "Bug Tracker": "https://github.com/HexyeDEV/EzTg/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["EzTg"],
    python_requires=">=3.6",
    install_requires=["aiohttp", "requests"],
)
