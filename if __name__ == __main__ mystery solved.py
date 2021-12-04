#note: when we import a file into another file, everything outside the 'if __name__ == "__main__"' block is executed in the original file. To stop that from executing, we put that in the 'if __name__ == "__main__"' block

import trailing #importing file
#note: this and the file being imported must be in the same folder

if __name__ == "__main__":
    print(trailing.zero_counter(10))
