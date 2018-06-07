import os
from math import ceil
from Crypto.Cipher import AES


# Thanks to https://julien.danjou.info/guide-python-static-class-abstract-methods/
class CryptText:

    @classmethod
    def crypt(cls, text_file, key):
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
                spaces = ' ' * ((16 * ceil(len(line)/16)) - len(line))
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
        :return:
        '''

        # Object for cli-decrypt configurations
        decryption = AES.new(key, AES.MODE_CBC, 'This is an IV456')

        # Load encrypted  file
        crypted_file = open(crypted_file, 'rb').read()

        print("Aquivo encripitaro: {}".format(crypted_file))

        # # with open(crypted_file, 'rb') as f:
        # #     crypted_lines = f.read()
        #
        # # Decrypt file
        # decrypt_lines = decryption.decrypt(crypted_lines).decode()

        decrypted_str = decryption.decrypt(crypted_file).decode()

        print (decrypted_str)

        return decrypted_str

