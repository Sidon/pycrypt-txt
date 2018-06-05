from setuptools import setup

setup(
    name='pycrypt-txt',
    packages = ['pycrypttxt', 'cli'],
    version='0.1.0',
    url='https://github.com/Sidon/pycrypt-txt',
    license='MIT License',
    author='Sidon Duarte',
    author_email='sidoncd@gmail.com',
    keywords='crypt django obfuscation',
    description='crypt and decrypt a txt file (useful for obfuscation django config)',
    install_requires=["pycrypto>=2.6"],

    entry_points={
        "console_scripts": [
            'pycryptext = cli.__main__:main'
        ]
    }

)
