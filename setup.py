import codecs

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='dataeng-msgtech',
    version="1.0",
    author='teja reddy',
    author_email='teja.reddy@msg.com',
    description="create dataeng pip package",
    packages=find_packages(),
    zip_safe=False,
    url=' https://github.com/ytkr/dataeng',
    long_description="",
)