import sys

from setuptools import setup

install_requires = [
    "aiohttp",
    "async_timeout"
]

setup(
    name="NAME",
    packages=["NAME"],
    install_requires=install_requires,
    version="0.0.1",
    description="A python3 library to communicate with XXXXX",
    python_requires=">=3.9.0",
    author="Daniel Hjelseth Høyer",
    author_email="mail@dahoiv.net",
    url="https://github.com/Danielhiversen/pyTemplate",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
