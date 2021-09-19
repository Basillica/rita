from setuptools import setup, find_packages


with open("README.md", encoding="utf8", errors='ignore') as f:
    long_description = f.read()

with open("requirements", encoding="utf8", errors='ignore') as f:
    install_requires = [l for l in f.readlines() if l and not l.startswith('#')]

setup(
    name='rita',
    version='0.0.1',
    author='Ezeabasili Anthony',
    author_email='ezeabasilianthony@gmail.com',
    license='MIT',
    description='A CLI tool for stock monitoring',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/basillica',
    py_modules=['rita'],
    packages=find_packages(),
    install_requires=install_requires,
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'rita = main:cli',
        ],
    },
)


  
# import re
# import setuptools

# with open('./requirements.in') as f:
#     install_requires = [l for l in f.readlines() if l and not l.startswith('#')]

# with open('./lepo/__init__.py', 'r') as infp:
#     version = re.search("__version__ = ['\"]([^'\"]+)['\"]", infp.read()).group(1)

# if __name__ == '__main__':
#     setuptools.setup(
#         name='lepo',
#         version=version,
#         url='https://github.com/akx/lepo',
#         author='Aarni Koskela',
#         author_email='akx@iki.fi',
#         maintainer='Aarni Koskela',
#         maintainer_email='akx@iki.fi',
#         license='MIT',
#         install_requires=install_requires,
#         packages=setuptools.find_packages('.', exclude=(
#             'lepo_tests',
#             'lepo_tests.*',
#         )),
#         include_package_data=True,
#     )