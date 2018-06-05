import os
from math import ceil
from Crypto.Cipher import AES


class CryptText():

    def crypt(self, text_file, output_crypted_file, key):

        print('file_imput: {} file_output: {} key: {}'.format(text_file, output_crypted_file, key))

        if not os.path.isfile(text_file):
            print('Input file (%s) does not exists ' % text_file)
            return

        # Create a encryptation suite
        encryption_suite = AES.new(key, AES.MODE_CBC, 'This is an IV456')

        fo = open(output_crypted_file, 'wb')
        with open(text_file, 'r') as f:
            for line in f:
                line.rstrip()
                spaces = ' ' * ((16 * ceil(len(line)/16)) - len(line))
                line += spaces
                cipher_text = encryption_suite.encrypt(line)
                fo.write(cipher_text)

    def decrypt(self, crypted_file, key):

        # Object for decrypt configurations
        decryption = AES.new(key, AES.MODE_CBC, 'This is an IV456')

        # Load encrypted  file
        with open(crypted_file,'rb') as f:
            crypt_conf = f.read()

        # Decrypt and convert to python dictionary
        decrypt_conf = decryption.decrypt(crypt_conf).decode()
        return decrypt_conf
