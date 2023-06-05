from setuptools import setup

with open('scripts/requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='slack-bot',
    version='1.0.0',
    author='The WUT PIS team',
    author_email='pis-wut-2023-best-team@gmail.com',
    description='Great package for detecting similar topics in slack conversations.',
    long_description='This package allows to employ a bot on a slack channel to detect similar messages.',
    long_description_content_type='text/markdown',
    url='https://github.com/wut-pis-2023/wut-pis-2023/tree/main',
    packages=['src/slack_bot'],
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
)