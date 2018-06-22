from setuptools import setup

setup(
    name = 'student-debt-trail',
    version = '0.1.0',
    packages = ['app'],
    entry_points = {
        'console_scripts': [
            'app = app.__main__:main'
        ]
    })
