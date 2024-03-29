from setuptools import setup


setup(
    packages=['fsh'],
    include_package_data=True,
    use_scm_version=True,
    install_requires=[
        'django',
        'django-cors-headers',
        'django-allauth',
        'django-rest-auth',
        'djangorestframework',
        'djangorestframework-jwt',
        'pygments',
        'Pillow',
        'pyyaml',
        'uritemplate',
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
