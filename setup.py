import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="parse-ingredients", # Replace with your own username
    version="0.0.4",
    author="Michiel K",
    author_email="",
    description="Parse strings of ingredients to their name, unit, quantity and optional comments.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MichielMag/parse-ingredients",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires='>=3.6',
)