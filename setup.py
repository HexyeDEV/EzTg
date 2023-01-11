import setuptools

long_description = "An api wrapper for telegram easy to use. Coerent according to telegram core.\n\nGithub: https://github.com/HexyeDev/EzTg\n\nDocumentation: https://eztg.readthedocs.io/en/latest/"

setuptools.setup(
    name="EzTg",
    version="0.2.2",
    author="Hexye",
    author_email="dragonsale22@gmail.com",
    description=
    "An api wrapper for telegram easy to use. Coerent according to telegram core.",
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
