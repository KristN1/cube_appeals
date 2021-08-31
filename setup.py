import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cube_appeals",
    version="0.2.6",
    author="KristN",
    author_email="kristndev@gmail.com",
    description="Python package for CubeCraft appeals page",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KristN1/cube_appeals",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          "undetected-chromedriver",
    ],

    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)