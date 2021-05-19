import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mxd84-pkg",
    version="0.0.dev1",
    author="Messa Daniele",
    author_email="messadaniele@gmail.com",
    description="A personal package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DaniMX125/MxD84",
    project_urls={
        "Bug Tracker": "https://github.com/DaniMX125/MxD84/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)