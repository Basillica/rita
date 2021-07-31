from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name='rita',
    version='0.0.1',
    author='Ezeabasili Anthony',
    author_email='ezeabasilianthony@gmail.com',
    license='MIT',
    description='A CLI for stock monitoring',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/basillica',
    py_modules=['rita', 'stock'],
    packages=find_packages(),
    install_requires=[requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        rita=main:main
    '''
)
