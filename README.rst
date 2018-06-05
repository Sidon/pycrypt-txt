``pycrypttxt`` - crypt and decrypt a txt file.
#######################################################


Description
***********

crypt and decrypt a txt file.
The primary goal for developing this project was obfuscation Django settings (json file).

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

::

   Crypt a file
   >>> from core.fcrypt import CryptText
   >>> crypt_text = CryptText()
   >>> crypt_text.crypt('input-file-name','output-file-name','a-16*n-digit-key')


Example:
########

::

   input-file.txt:
    {
      "secretk": "w6**ci+meh34=n)o_299ee5qga7ubb&pb30=iyx^5$+v-_iv+u)!nw",
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

   Crypt a file
   >>> from core.fcrypt import CryptText
   >>> crypt_text = CryptText()
   >>> crypt_text.crypt('input-file.txt','output-file.bin','1234567890123456')



:Authors:
    Sidon Duarte,

:Version: 0.0.1 of 2018/06/04
