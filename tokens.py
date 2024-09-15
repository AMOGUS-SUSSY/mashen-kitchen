import os
import numpy as np
import argparse
from tqdm import tqdm
from collections import Counter

# RUN FROM MASHEN KITCHEN
VOCAB = "languini/vocabs/spm_models/"

def count(file):
    tokens = np.load(file)
    c = Counter(tokens)
    return c

def main(data_root,vocab,vocab_size, output):
    c = Counter()
    print("Counting...")
    for root, dirs, files in tqdm(os.walk(data_root)):
        for file in tqdm(files):
            c.update(count(os.path.join(data_root,file)))
    print("Writing...")
    open(output, 'w')
    vocab = open(VOCAB+vocab, 'r')
    lines = vocab.readlines()
    with open(output, 'a') as out:
        i = 1
        for element in tqdm(c.most_common(vocab_size)):
            temp = [x for x in element]
            out.write('  '.join(['top'+str(i),lines[temp[0]].strip('\n'),str(temp[1]),'\n']))
            i += 1
    print("DONE")

if __name__ == "__main__":
    # Use argparse to get command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_root", required=True, help="path to all the tokenised files")
    parser.add_argument("--vocab", required=True, help="vocab-name")
    parser.add_argument("--vocab_size", required=True, type=int, help="vocabulary size")
    parser.add_argument("--output", required=True, help="file to write stuff into")
    args = parser.parse_args()

main(args.data_root, args.vocab, args.vocab_size, args.output)
