import os
import sys

def directory_tree(path):
    for root,dirs,files in os.walk(path):
        level = root.replace(path,'').count(os.sep)
        print(" " * 2 * level,end='')
        if level != 0:
            print("- ",end='')
        print(os.path.basename(root))
        for f in files:
            print(" "*2*(level+1),end='')
            print("- "+f)        

def main():
    if len(sys.argv)!=2:
        print("Format : python3 tree.py <directory path>")
    path = os.path.realpath(sys.argv[1])
    directory_tree(path)

if __name__ == "__main__":
    main()