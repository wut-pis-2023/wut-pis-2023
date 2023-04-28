from setuptools import setup

with open('scripts/requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='slack-bot',
    version='1.4.2',
    author='Your Name',
    author_email='pis-wut-2023-best-team@example.com',
    description='Great package for detecting similar topics in slack conversations.',
    long_description='This package allows ',
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/yourpackage',
    packages=['src/slack-bot'],
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
)
