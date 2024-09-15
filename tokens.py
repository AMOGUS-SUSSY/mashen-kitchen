import os
import numpy as np
import argparse
from collections import Counter

# RUN FROM MASHEN KITCHEN
IN = "data/mashen/pre_16284"

def count(file):
    tokens = np.load(file)
    c = Counter(tokens)
    return c

def main(data_root,vocab_size):
    c = Counter()
    for root, dirs, files in os.walk(data_root):
        for file in files:
            c.update(count(np.load(os.path.join(data_root,file))))
    with open("output.txt", 'a') as out:
        for element in c.most_common(vocab_size):
            out.write(element + "\n")

if __name__ == "__main__":
    # Use argparse to get command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_root", required=True, help="path to all the tokenised files")
    parser.add_argument("--vocab_size", required=True, help="vocabulary size")
    args = parser.parse_args()

main(args.data_root, args.vocab_size)
