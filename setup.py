
from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='gazeboMAP',
    version='1.0.0',
    packages=['gazeboplanner', 'gazeboplanner.gadapter'],
    package_dir={'gazeboplanner': 'src'},
    url='http://cog-isa.github.io/mapplanner/',
    license='',
    author='KiselevGA',
    author_email='kiselev@isa.ru',
    long_description=open('README.md').read(),
    install_requires=required
)