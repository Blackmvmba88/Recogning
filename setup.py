"""
Setup configuration for Recogning
"""

from setuptools import setup, find_packages
import pathlib

# Read README for long description
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

# Read requirements
requirements = []
# Requirements will be added in PHASE 1+
# requirements = (here / "requirements.txt").read_text().splitlines()

setup(
    name="recogning",
    version="0.0.1",
    description="El Aprendiz Cuántico Visual del Mundo Físico",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Blackmvmba88/Recogning",
    author="BlackMamba",
    author_email="",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="computer-vision, object-detection, visual-memory, ai, deep-learning, yolo, clip",
    packages=find_packages(exclude=["tests", "docs", "examples", "scripts"]),
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.7.0",
            "flake8>=6.1.0",
            "mypy>=1.5.0",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/Blackmvmba88/Recogning/issues",
        "Source": "https://github.com/Blackmvmba88/Recogning",
        "Documentation": "https://github.com/Blackmvmba88/Recogning/wiki",
    },
    entry_points={
        "console_scripts": [
            # CLI commands will be added in PHASE 1+
            # "recogning=recogning.cli:main",
        ],
    },
)
