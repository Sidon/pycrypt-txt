import argparse
from core.fcrypt import CryptText

parser = argparse.ArgumentParser()
parser.add_argument("inputfile", help="File to be encrypted")
parser.add_argument("outputfile", help='Encrypted output file')
parser.add_argument("key", help="Encryption key 16, 24, or 32 bytes long")

args = parser.parse_args()


def main(args):

    # Open output file
    fo = open(args.outputfile, 'w')

    # deCrypt the input file
    decrypted_text = CryptText.decrypt(args.inputfile, args.key)

    # save the encrypted inputed file
    fo.write(decrypted_text )


if __name__ == "__main__":
    main(args)
