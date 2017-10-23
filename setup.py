from setuptools import setup, find_packages

install_requires = [
    'redis~=2.8.0',
    'https://github.com/vartec/example_repo_setuptools_issue_submodule',
]


tests_require = [
    'pytest',
]


setup(
    name='example_module',
    version='0.1.0',
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=tests_require,
    setup_requires=['pytest-runner'],
    extras_require={
        'testing': tests_require,
    },
)
