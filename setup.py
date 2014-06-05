"""The setup and build script for the pyadmitad library."""
import io
import os
from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

__author__ = 'trezorg@gmail.com'
__version__ = '0.0.1'

def read(*names, **kwargs):
    return io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()

setup(
    name="pyadmitad",
    version=__version__,
    author='Igor Nemilentsev',
    author_email='trezorg@gmail.com',
    description='A Python wrapper around the Admitad API',
    long_description=read('README.md'),
    license='MIT',
    url='https://github.com/trezorg/admitad-python-api.git',
    keywords='admitad',
    packages=find_packages(exclude=['*tests*', '*.tests']),
    include_package_data=True,
    install_requires=['requests'],
    test_suite='nose.collector',
    tests_require=['nose', 'mocker'],
    setup_requires=['nose'],
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

