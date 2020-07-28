from setuptools import setup


setup(
    packages=['fsh'],
    include_package_data=True,
    use_scm_version=True,
    install_requires=[
        'django',
        'django-pygmentify',
        'django-cors-headers',
        'djangorestframework',
        'djangorestframework-jwt',
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
