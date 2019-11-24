from setuptools import setup
from codecs import open  # To use a consistent encoding
from os import path

from m2r import parse_from_file

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
readme = parse_from_file(path.join(here, 'README.md'), encoding='utf-8')

setup(
    name='quicks',

    version='0.0.1',

    description='Python module to generate project',
    long_description=readme,
    long_description_content_type='text/x-rst',

    url='https://github.com/daxartio/quicks',

    # Author details
    author='Akhtarov Danil',
    author_email='daxartio@gmail.com',

    # Choose your license
    license='GPLv3+',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: System :: Hardware :: Hardware Drivers',

        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    # What does your project relate to?
    keywords='quicks generator',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['quicks'],

    # List run-time dependencies here.  These will be installed by pip when your
    # project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/technical.html#install-requires-vs-requirements-files
    install_requires=['PyYAML'],
    entry_points={
        'console_scripts': ['quicks=quicks.__main__:main'],
    }
)