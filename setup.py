import setuptools

setuptools.setup(
    
    name="attribution",
    version="0.0.1",
    url="https://github.com/sliao888/perfAttribution",
    author="sliao",
    author_email="simon.liao19@gmail.com",
    description="Performance Attribution",
    long_description=open("README.md").read(),
    license='MIT',
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=setuptools.find_packages(),
    package_data={'attribution': ['Data/*.csv', 'Templates/*.xlsx']},
    classifiers=[
        "Programming Language :: Python :: 3.6"
    ],
    py_modules=['attribution'],
    python_requires='>=3.6',
    install_requires=['pandas>=1.0.3',
                      'numpy>=1.18.1']

)