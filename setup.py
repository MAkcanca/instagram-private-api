from os import path
import io
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    import unittest.mock
    has_mock = True
except ImportError:
    has_mock = False

__author__ = 'makcanca'
__version__ = '1.0.0'

packages = [
    'instagram_private_api',
    'instagram_private_api.endpoints',
]
test_reqs = [] if has_mock else ['mock']

setup(
    name='instagram_private_api',
    version=__version__,
    author='makcanca',
    author_email='',
    license='BSD',
    url='',
    install_requires=[],
    test_requires=test_reqs,
    keywords='instagram private api',
    description='',
    long_description='',
    long_description_content_type='text/markdown',
    packages=packages,
    platforms=['any'],
    classifiers=[
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
