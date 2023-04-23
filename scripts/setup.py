from setuptools import setup

with open('scripts/requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='slack-bot',
    version='1.2.0',
    author='Your Name',
    author_email='youremail@example.com',
    description='A short description of your package',
    long_description='description',
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
