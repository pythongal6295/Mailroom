import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mailroom",
    version="0.0.2",
    author="Kelly Kauffman",
    author_email="kellyk20@uw.edu",
    description="stores donor information, writes thank yous, creates reports",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UWPCE-Py310-Fall2020/mailroom-everything-pythongal6295",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    #packages = ["C:/Users/kelly_kjenkz1/UW_Python_310A/Lesson_05/mailroom-everything-pythongal6295/mailroom"]
    scripts = ["bin/mailroom_main.py"]
)
