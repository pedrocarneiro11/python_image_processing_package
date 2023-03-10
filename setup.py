from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.2",
    author="Pedro Carneiro",
    author_email="pedrocarneirocunha87@gmail.com",
    description="pacote de processamento de imagens em Python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pedrocarneiro11/python_image_processing_package",
    Homepage="https://github.com/pedrocarneiro11/python_image_processing_package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
