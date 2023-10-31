import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="spetslogging",
    version="alfa-1.0",
    author="Dmitry",
    author_email="dinamition42@gmail.com",
    description="SpetsLogging is a simple way to log in the console and in a file.",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DiNAMitiON/SpetsLogging",
    packages=['spetsloging'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
    ],
    python_requires='>=3.5',
)
