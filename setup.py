from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'A package for various types of timers'

with open("README.md", "r") as file:
    long_description = file.read()

URL = 'https://github.com/FrickTzy/Pygame-Timer'

setup(
    name="pygame_timer",
    version=VERSION,
    author="FrickTzy (Kurt Arnoco)",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    url=URL,
    install_requires=['pygame'],
    keywords=['python', 'pygame', 'python game', 'python game development', 'pygame timer'],
)