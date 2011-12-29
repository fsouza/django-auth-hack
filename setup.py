from setuptools import setup
from auth_hacks import __version__

README = open('README.rst').read()

setup(name='django-auth-hack',
      version=__version__,
      description="Hacking Django's contrib auth app to support longer usernames",
      long_description=README,
      author='Francisco Souza',
      author_email='francisco@franciscosouza.net',
      packages=['auth_hacks'],
      include_package_data=True,
      install_requires=['Django>=1.3.1'],
      )

