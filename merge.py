import os
import glob 
from PyPDF2 import PdfMerger, PdfReader

def main():
    inp = input("""
    [0] Merge PDFS in input folder
    [1] List documents to be merged
    """)

    if int(inp) == 0:
        order = input("""
        Specify order:
        [0] Date
        [1] Alphabetical
        """)
        if (int(order) == 0):
            files = list(filter(os.path.isfile, glob.glob("in/*")))
            files.sort(key=lambda x: os.path.getmtime(x))
            merge_files(files)
        elif (int(order) == 1):
            files = os.listdir("in/")
            for i in range(len(files)):
                files[i] = "in/" + files[i]
            merge_files(sorted(files))
        else:
            print("Illegal input. Closing")
    elif int(inp) == 1:
        files = []
        file_name = ""
        print("Please list out the full path and name of your file. Type in \"d\" when done")
        while (True):
            file_name = input()
            if (file_name == "d"):
                break
            if (not os.path.isfile(file_name)):
                print("File doesn't exist. Try again.")
                continue
            files.append(file_name)
        merge_files(files)
    else:
        print("Illegal input. Closing")
        main()

def merge_files(files):
    merger = PdfMerger()
    for filename in files:
        merger.append(PdfReader(open(filename, 'rb')))
    merger.write(os.path.abspath("result.pdf"))

if __name__ == "__main__":
    main()
