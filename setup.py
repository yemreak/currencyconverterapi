from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup

VERSION = "1.0.0"
README_PATH = "README.md"

# test_requirements = ["behave", "behave-classy", "pytest"]

long_description = ""
with open(README_PATH, "r", encoding="utf-8") as file:
    long_description = file.read()

setup(
    name="currecyconverterapi",
    version=VERSION,
    license="Apache Software License 2.0",
    description="Simplest currency converter with pure python with CurrecnyConverterApi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Yunus Emre Ak",
    author_email="yemreak.com@gmail.com",
    url="https://github.com/yedhrab/currencyconverterapi",
    packages=find_packages(),
    py_modules=[splitext(basename(path))[0] for path in glob("*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Utilities",
    ],
    project_urls={
        "Changelog": "https://github.com/yedhrab/currecyconverterapi/blob/master/CHANGELOG.md",
        "Issue Tracker": "https://github.com/yedhrab/currecyconverterapi/issues",
    },
    keywords=["currencyconverter", "conveter", "currecies"],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    entry_points={"console_scripts": ["convert = currencyconverterapi.__init__:main"]},
)
