from setuptools import setup

setup(
    name="pyadmitad",
    packages=['pyadmitad'],
    version='1.0.0',
    author='Admitad Dev Bot',
    author_email='dev@admitad.com',
    description='A Python wrapper around the Admitad API',
    license='MIT',
    url='https://github.com/admitad/admitad-python-api.git',
    keywords='admitad',
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
