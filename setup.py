from setuptools import setup, find_packages

setup(
    name="tnxadnan-esp", # The name users will use: pip install my-universal-esp
    version="0.1.0",
    author="Your Name",
    description="A library for memory-based ESP in games",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/yourrepo", # Optional
    packages=find_packages(),
    install_requires=[
        "pymem",
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.6',
)