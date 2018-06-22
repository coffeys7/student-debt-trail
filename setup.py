from setuptools import setup

setup(
    name = 'student_debt_trail',
    version = '0.1.0',
    packages = ['student_debt_trail'],
    entry_points = {
        'console_scripts': [
            'student_debt_trail = student_debt_trail.__main__:main'
        ]
    })
