from setuptools import setup


requires = ["matplotlib","networkx", "numpy"]


setup(
    name='reserch_utils_HT',
    version='0.1',
    description='complex network model, graph to image utils',
    url='https://github.com/whatever/whatever',
    author='HayatoTanoue',
    author_email='hayatotanoue7321@gmail.com',
    license='MIT',
    keywords='complex networks',
    packages=[
        "your_package",
        "your_package.subpackage",
    ],
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)