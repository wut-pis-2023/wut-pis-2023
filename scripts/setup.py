from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='my-package',
    version='1.0.0',
    author='Your Name',
    author_email='youremail@example.com',
    description='A short description of your package',
    long_description='description',
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/yourpackage',
    packages=['mypackage'],
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
