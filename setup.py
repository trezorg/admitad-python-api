"""The setup and build script for the pyadmitad library."""
from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

__author__ = 'dev@admitad.com'
__version__ = '1.0.0'

setup(
    name="pyadmitad",
    version=__version__,
    author='Admitad Dev Bot',
    author_email='dev@admitad.com',
    description='A Python wrapper around the Admitad API',
    license='MIT',
    url='https://github.com/admitad/admitad-python-api.git',
    keywords='admitad',
    packages=find_packages(exclude='tests'),
    install_requires=['requests', 'simplejson'],
    test_suite='nose.collector',
    tests_require=['nose', 'mocker'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications',
        'Topic :: Internet',
    ],
    dependency_links=[
        "git+https://github.com/trezorg/mocker.git#egg=mocker",
    ],
)

