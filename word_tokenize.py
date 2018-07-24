import argparse
import os

from util.crf.word_tokenize import word_tokenize

parser = argparse.ArgumentParser("word_tokenize.py")
text_group = parser.add_argument_group("The following arguments are mandatory for text option")
text_group.add_argument("--text", metavar="TEXT", help="text to predict")
file_group = parser.add_argument_group("The following arguments are mandatory for file option")
file_group.add_argument("--fin", help="file input")
file_group.add_argument("--fout", help="file output")
parser.add_argument("--model", help="path to saved model")

args = parser.parse_args()

if __name__ == '__main__':
    if not (args.text or args.fin):
        parser.print_help()

    if args.text:
        text = args.text
        label = word_tokenize(text, format="text")
        print(label)

    if args.fin or args.fout:
        if not (args.fout and args.fin):
            parser.error("Options --fin and --fout must be set together")
        file_in = args.fin
        file_out = args.fout
        try:
            os.rm(args.fout)
        except:
            pass
        f = open(file_out, "a")
        for text in open(file_in):
            text = text.strip()
            output = word_tokenize(text, format="text") + "\n"
            f.write(output)