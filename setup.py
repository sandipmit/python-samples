import setuptools

setuptools.setup(
    name = "sandipPythonSamples",
    version = "0.0.1",
    author = "sandip",
    author_email = "author@example.com",
    description = "test package",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)