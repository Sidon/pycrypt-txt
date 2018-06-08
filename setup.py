from setuptools import setup

setup(
    name='py-sdncrypt',
    packages = ['pysdncrypt', 'clicrypt', 'clidecrypt', 'clijsonminify'],
    version='0.1.0',
    url='https://github.com/Sidon/pycrypt-txt',
    license='MIT License',
    author='Sidon Duarte',
    author_email='sidoncd@gmail.com',
    keywords='clicrypt django obfuscation',
    description='Minify a json file, encrypt and decrypt a txt file (useful for obfuscation django config)',
    install_requires=["pycrypto>=2.6"],

    entry_points={
        "console_scripts": [
            'sdnjsonminify = clijsonminify.__main__:main',
            'sdncrypt = clicrypt.__main__:main',
            'sdndecrypt = clidecrypt.__main__:main',
        ]
    }

)
