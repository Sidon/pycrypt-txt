import os
from math import ceil
from Crypto.Cipher import AES


class Cryptjson():

    def crypt(self, file_input, file_output, key):

        print('file_imput: {} file_output: {} key: {}'.format(file_input, file_output, key))


        if not os.path.isfile(file_input):
            print('Input file (%s) does not exists ' % file_input)
            return

        # Create a encryptation suite
        # encryption_suite = AES.new(os.environ['MASTERKEY'], AES.MODE_CBC, 'This is an IV456')
        encryption_suite = AES.new(key, AES.MODE_CBC, 'This is an IV456')


        fo = open(file_output, 'wb')
        with open(file_input, 'r') as f:
            for line in f:
                line.rstrip()
                spaces = ' ' * ((16 * ceil( len(line)/16)) - len(line))
                line += spaces
                cipher_text = encryption_suite.encrypt(line)
                fo.write(cipher_text)
