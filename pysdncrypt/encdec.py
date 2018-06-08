import os
import json
from math import ceil
from Crypto.Cipher import AES


# Thanks to https://julien.danjou.info/guide-python-static-class-abstract-methods/
class CryptText:

    @classmethod
    def encrypt(cls, text_file, key):
        '''
        Encrypt a text file
        :param text_file: File that will be encrypted
        :param key: Encryption key 16, 24, or 32 bytes long
        :return: List of encrypted lines
        '''

        if not os.path.isfile(text_file):
            print('Input file (%s) does not exists ' % text_file)
            return

        # Create a encryptation suite
        encryption_suite = AES.new(key, AES.MODE_CBC, 'This is an IV456')

        encrypt_lines = []

        # fo = open(output_crypted_file, 'wb')
        with open(text_file, 'r') as f:
            for line in f:
                line.rstrip()
                spaces = ' ' * ((16 * ceil(len(line) / 16)) - len(line))
                line += spaces
                cipher_text = encryption_suite.encrypt(line)
                encrypt_lines.append(cipher_text)

        return encrypt_lines

    @classmethod
    def decrypt(cls, crypted_file, key):
        '''
        Decrypt a text file
        :param crypted_file: File that will be decrypted
        :param key: Encryption key 16, 24, or 32 bytes long
        :return: Decrypted String
        '''

        # Object for clidecrypt configurations
        decryption = AES.new(key, AES.MODE_CBC, 'This is an IV456')

        # Load encrypted  file
        crypted_file = open(crypted_file, 'rb').read()

        decrypted_str = decryption.decrypt(crypted_file).decode()

        return decrypted_str


    @classmethod
    def minifyjson(cls, input_file, output_file):
        '''
        Minify a json file
        :param input_file:
        :param output_file:
        :return: True (for success) of False
        '''

        if not os.path.isfile(input_file):
            print('Input file (%s) does not exists ' % input_file)
            return False

        # Open inputfile
        json_input = open(input_file, 'r').read()

        # Minify
        json_mini = json.dumps(json.loads(json_input), separators=(',', ':'))

        # save the encrypted inputed file
        open(output_file, 'w').write(json_mini)

        return True
