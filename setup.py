import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="abstools",
    version="0.0.1",
    author='Bruce Cauchi',
    author_email="",
    description='Tools that help out working with ABS (Australian Bureau of Statistics) data',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Zir01/abstools',
    license='BSD License',
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        'Development Status :: Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: BSD License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)