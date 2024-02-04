from setuptools import setup, find_packages

setup(
    name='DjRetailHub',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='A Django app to analyze and visualize sales data.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='[Your Name]',
    author_email='[Your Email]',
    url='https://github.com/Charl12-gb/djretailhub',
    install_requires=[
        'Django>=3.2',
    ],
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
)
