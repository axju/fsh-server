from setuptools import setup, find_packages


setup(
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    include_package_data=True,
    use_scm_version=True,
    install_requires=[
        'django',
        'django-crispy-forms',
        'django-pygmentify',
    ],
    setup_requires=[
        'setuptools_scm',
    ],
    entry_points={
        'console_scripts': [
            'fsh=fsh.__main__:main',
        ],
    },
)
