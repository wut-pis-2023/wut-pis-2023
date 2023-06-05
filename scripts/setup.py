from setuptools import setup, find_packages

with open('scripts/requirements.txt') as f:
    requirements = f.read().splitlines()

print("FOUND PACKAGES", find_packages())

setup(
    name='slack-bot',
    version='1.5.1',
    author='The WUT PIS team',
    author_email='pis-wut-2023-best-team@gmail.com',
    description='Great package for detecting similar topics in Slack conversations.',
    long_description='This package allows to employ a bot on a slack channel to detect similar messages.',
    long_description_content_type='text/markdown',
    url='https://github.com/wut-pis-2023/wut-pis-2023/tree/main',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Communications :: Chat',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
