from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-plugin-ld",
    description="null",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Redmer Kronemeijer",
    url="https://github.com/redmer/datasette-plugin-ld",
    project_urls={
        "Issues": "https://github.com/redmer/datasette-plugin-ld/issues",
        "CI": "https://github.com/redmer/datasette-plugin-ld/actions",
        "Changelog": "https://github.com/redmer/datasette-plugin-ld/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License"
    ],
    version=VERSION,
    packages=["datasette_plugin_ld"],
    entry_points={"datasette": ["plugin_ld = datasette_plugin_ld"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    python_requires=">=3.7",
)
