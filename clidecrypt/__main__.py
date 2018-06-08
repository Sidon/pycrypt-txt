import argparse
from pysdncrypt.encdec import CryptText
parser = argparse.ArgumentParser()
parser.add_argument("inputfile", help="File to be encrypted")
parser.add_argument("outputfile", help="File to be encrypted")
parser.add_argument("key", help="Encryption key 16, 24, or 32 bytes long")

args = parser.parse_args()


def main():

    # deCrypt the input file
    decrypted_text = CryptText.decrypt(args.inputfile, args.key)

    # Open output file
    fo = open(args.outputfile, 'w')

    # save the encrypted inputed file
    fo.write(decrypted_text)
    fo.close()

    print("Successful Encryption, {} encrypted to {}".format(args.inputfile, args.outputfile))


if __name__ == "__main__":
    main()

