import setuptools

setuptools.setup(
    name="robocupRAI",
    version="1.2",
    author="whaly",
    author_email="whalykj@gmail.com",
    description="A small example package MongoDB Robo",
    long_description='long_description',
    long_description_content_type="text/markdown",
    url="https://github.com/whaly-w/robocup",
    packages=setuptools.find_packages(),
    install_requires=[
        'dnspython',
        'install',
        'pymongo'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)