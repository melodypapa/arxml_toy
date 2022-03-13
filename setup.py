"""Minmal setup file for Version Manager"""

from setuptools import setup, find_packages

setup(
    name='arxml_toys',
    version = '1.0.0',
    license = 'BSD',
    description="Power Toys for the ARXML",

    author = 'Zhang Lei',
    author_email = "lei.23.zhang@continental-corporation.com",
    url="",

    packages = find_packages(where='src'),
    package_dir= {'': 'src'},

    include_package_data=True,
    
    extras_require={'pytest': 'pytest-cov'},

    entry_points={
        'console_scripts': [
            'arxml_uuid = cli.uuid_cli:main',
            'arxml_timestamp = cli.timestamp_cli:main',
        ]
    }
)