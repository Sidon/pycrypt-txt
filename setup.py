from setuptools import setup

setup(
    name='pycrypttxt',
    version='0.1.0',
    url='https://github.com/sidon/pycryptjs',
    license='MIT License',
    author='Sidon Duarte',
    author_email='sidoncd@gmail.com',
    keywords='crypt django obfuscation',
    description='crypt and decrypt a txt file (useful for obfuscation django config)',
    packages=['pycryptjs'],
    install_requires=[pycrypto==2.6.1],
)
