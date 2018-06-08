``pycrypttxt`` - crypt and decrypt a txt file.
#######################################################


Description
***********

Minify a json file, crypt and decrypt a txt file.
The primary goal for developing this project was obfuscation Django settings (json file).

:Authors:
    Sidon Duarte,

:Version: 0.0.1 of 2018/06/04


Requirements
************

::

    Python 3
    pycrypto==2.6.1


Environment (of development)
****************************

::

    LSB Version:    core-9.20170808ubuntu1-noarch:security-9.20170808ubuntu1-noarch
    Distributor ID: Ubuntu
    Description:    Ubuntu 18.04 LTS
    Release:        18.04
    Codename:       bionic


Install
#######

::

    TODO


Usage
#####


Minify a json file
*******************

::

    Original file:
    {
      "secretk": "qq6**ci+meh34=n)o_299ee523ga7ubb&pb30=iyx^5$+v-_iv+u)!nw",
      "debug": "on",
      "ahosts": "localhost,127.0.0.1",
      "add_apps": ["django_extensions"],

       "db": {
         "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "my-database",
            "USER": "database-user",
            "PASSWORD": "password-99",
            "HOST": "localhost",
            "PORT": "5432"
         }
       }
    }

    >>> from pysdncrypt.encdec import CryptText
    >>> CryptText.minifyjson('original-file', 'original-file-mini')
    True

Encrypt a txt file
*******************

::

    >>>> crypted_file = CryptText.encrypt('original-mini', '0123456789012345')



Dencrypt a txt file
*******************

::

    >>>> crypted_file = CryptText.decrypt('file-crypted', '0123456789012345')


Line Commands
##############


::

    Minifing a json file:
    -----------------------
    $ sdnjsonminify config-original config-minify
    Successful minification, config-original minified to config-minify

    Encrypting a text file:
    -----------------------
    $ sdnencrypt config-original-mini config-original-mini-encrypted 0123456789012345
    Successful Encryption, config-original-mini encrypted to config-original-mini-encrypted

    Decrypting a text file:
    -----------------------
    $ sdndecrypt config-original-mini-encrypted config-original-mini-decrypted 0123456789012345
    Successful Encryption, config-original-mini-encrypted encrypted to config-original-mini-decrypted