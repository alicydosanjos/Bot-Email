"""
Setup script para o Email Auto-Response System
"""

from setuptools import setup, find_packages
import os

# Ler README
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Ler requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="email-auto-response-system",
    version="1.0.0",
    author="Seu Nome",
    author_email="seu.email@exemplo.com",
    description="Sistema inteligente de Machine Learning para classificação e resposta automática de emails",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/seu-usuario/email-auto-response-system",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Communications :: Email",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    entry_points={
        "console_scripts": [
            "email-auto-response=run:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.yml", "*.yaml"],
    },
    keywords="email, machine learning, classification, auto response, nlp, streamlit",
    project_urls={
        "Bug Reports": "https://github.com/seu-usuario/email-auto-response-system/issues",
        "Source": "https://github.com/seu-usuario/email-auto-response-system",
        "Documentation": "https://github.com/seu-usuario/email-auto-response-system#readme",
    },
)
