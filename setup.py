"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
import os

from setuptools import find_packages, setup

from rabbit_queues import __version__

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

REQUIREMENTS = [
    "Django==3.1.7",
    "pika==1.2.0",
]

setup(
    name="rabbit_queues",
    version=__version__,
    author="Rafal Przetakowski",
    description="Application to manage RabbitMQ queues",
    long_description=open("README.md").read(),
    packages=find_packages(),
    url="https://github.com/beeflow/rabbit_queues.git",
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
)
