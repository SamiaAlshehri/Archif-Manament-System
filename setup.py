from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in archif_managment/__init__.py
from archif_managment import __version__ as version

setup(
	name="archif_managment",
	version=version,
	description="this app mange your data and arrang it in simple way and make category for all kind of your data or books",
	author="Samia Nasser",
	author_email="alshehri2engsam@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
