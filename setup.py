import setuptools

setuptools.setup(
    name="perfAttribution",
    version="0.0.1",
    author="sliao",
    author_email="simon.liao19@gmail.com",
    description="Performance Attribution",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6"
    ],
    python_requires='>=3.6',

)