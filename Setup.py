from setuptools import setup, find_packages


setup(
        name='TestsHardCode',
        version='0.0.1',
        description='This module was written for tests',
        author='Kirill Kudinov',
        license='MIT',
        url='https://github.com/XxXDeathmatchXxX/TestsHardCode',
        packages=find_packages(exclude=['random, math']),
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        classifiers=[
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.9',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )