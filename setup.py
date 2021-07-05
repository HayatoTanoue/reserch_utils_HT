from setuptools import setup, find_packages

import reserch_utils_HT
requires = ["matplotlib","networkx", "numpy"]


setup(
    name='reserch_utils_HT',
    version=reserch_utils_HT.__version__,
    description='complex network model, graph to image utils',
    url='https://github.com/HayatoTanoue/reserch_utils_HT',
    author=reserch_utils_HT.__author__,
    author_email='hayatotanoue7321@gmail.com',
    license=reserch_utils_HT.__license__,
    keywords='complex networks',
    packages=find_packages(),
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)