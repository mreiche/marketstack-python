from setuptools import setup

from marketstack import __version__

setup(
    name='marketstack',
    version=__version__,

    url='https://github.com/mreiche/marketstack',
    author='Mike Reiche',
    author_email='mike@reiche.world',

    py_modules=['marketstack'],
    install_requires=[
        'pydantic>=1.9.1',
        'requests>=2.28.1'
    ],
    extra_test=[
        'pytest>=7.1.3',
    ]
)
