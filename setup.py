import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyhomepilot",
    version="0.0.3",
    author="Nicolas Gres",
    author_email="nicolas@gres.io",
    description="Unofficial Rademacher HomePilot API wrapper",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nico0302/pyhomepilot",
    install_requires=[
        "aiohttp",
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
