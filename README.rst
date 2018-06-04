``pycryptjson`` - crypt and decrypt a jason file.
#######################################################


Description
***********

crypt and decrypt a jason file.
The primary goal for developing this project was obfuscation Django settings.

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

   Crypt a file
   >>>>from core.fcrypt import Cryptjson
   >>>>c1 = Cryptjson()
   >>>>c1.crypt('input-file-name','output-file-name','a-16*n-digit-key')

:Authors:
    Sidon Duarte,

:Version: 0.0.1 of 2018/06/04
