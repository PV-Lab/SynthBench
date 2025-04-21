from setuptools import setup, find_packages

setup(
    name='synthbench',
    version='0.1.0',
    description='A synthetic hypothesis testing environment for testing synthesizability filters.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Basita Das',
    author_email='dasb@mit.edu',
    url='https://github.com/PV-Lab/SynthBench',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)