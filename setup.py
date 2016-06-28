from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '0.1.1'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
  long_description = f.read()


install_requires = ['mongoengine>=0.8.0']
test_requirements = ['nose', 'rednose', 'coverage', 'mongomock']


setup(
  name='mongocapsule',
  version=__version__,
  description='Encapsulated MongoEngine.',
  long_description=long_description,
  url='https://github.com/prashnts/mongocapsule',
  download_url='https://github.com/prashnts/mongocapsule/tarball/' + __version__,
  license='MIT',
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules'
  ],
  keywords='',
  packages=['mongocapsule'],
  include_package_data=True,
  author='Prashant Sinha',
  install_requires=install_requires,
  tests_require=test_requirements,
  author_email='prashant@ducic.ac.in'
)
