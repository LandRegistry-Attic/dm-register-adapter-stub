from setuptools import setup, find_packages

setup(
    name="regad_stub",
    version="0.1",
    author="Fix Me",
    author_email="fix.me@landregistry.gsi.gov.uk",
    packages=find_packages(),
    install_requires=["flask"],
    tests_require=["flask"],
    test_suite="regad_stub.test_suite.suite",
    entry_points={'console_scripts':
                  ['regad_stub = regad_stub.main:main']}
)
