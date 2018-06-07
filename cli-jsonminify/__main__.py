import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("inputfile", help="File to be encrypted")
parser.add_argument("outputfile", help='Encrypted output file')

args = parser.parse_args()

def main(args):


    # Open inputfile
    json_input = open(args.inputfile, 'r').read()
    json_mini = json.dumps(json.loads(json_input), separators=(',', ':'))

    # save the encrypted inputed file
    open(args.outputfile, 'w').write(json_mini)

    print("Successful minification, {} minified to {}".format(args.inputfile, args.outputfile))


if __name__ == "__main__":
    main(args)







@classmethod
def diff_json(cls, _file1, _file2):

    json_mini = json.dumps(json.loads(json_txt), separators=(',', ':'))
