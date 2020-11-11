#!/home/franck/anaconda3/bin/python

import sys

def main():

    wordcount = dict()
    line = sys.stdin.readline()
    while line:
        word = line.split("\t")
        wordcount[word[0]] = wordcount.get(word[0],0)+1
        line = sys.stdin.readline()
    
    for key, value in wordcount.items():
        print("%s\t%d"%(key,value))
            
if __name__ == "__main__":

    main()
