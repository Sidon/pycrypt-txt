import argparse
from pysdncrypt.encdec import CryptText
parser = argparse.ArgumentParser()
parser.add_argument("inputfile", help="File to be encrypted")
parser.add_argument("outputfile", help='Encrypted output file')

args = parser.parse_args()


def main():

    CryptText.minifyjson(args.inputfile, args.outputfile)
    # # Open inputfile
    # json_input = open(args.inputfile, 'r').read()
    #
    # # Minify
    # json_mini = json.dumps(json.loads(json_input), separators=(',', ':'))
    #
    # # save the encrypted inputed file
    # open(args.outputfile, 'w').write(json_mini)
    #
    print("Successful minification, {} minified to {}".format(args.inputfile, args.outputfile))


if __name__ == "__main__":
    main()

