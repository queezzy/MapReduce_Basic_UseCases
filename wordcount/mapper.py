#!/home/franck/anaconda3/bin/python
import sys
import re


def main():
    
    line = sys.stdin.readline()

    while line:
        words = re.split(r"\W+",line.strip())
        for word in words :
            if len(word)>0:
                print(word+"\t"+"1")
        line = sys.stdin.readline()
            
if __name__ == "__main__":

    main()
