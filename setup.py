from setuptools import setup

setup(
    name='dbt-redhshift-dryrun',
    version='0.1.0',    
    description='Python package dry running redshift queries',
    url='https://github.com/shassaan/dbt-redshift-dryrun',
    author='Syed Hassaan Ahmed',
    author_email='syedhassaan.103@gmail.com',
    license='BSD 2-clause',
    packages=['dbt-redhshift-dryrun'],
    install_requires=[],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)