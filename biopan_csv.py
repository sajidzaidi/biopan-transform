import sys
import csv 

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print("biopan_csv.py inputfile outputfile")
        exit(1)
    input_file= sys.argv[0]
    output_file=sys.argv[1]

    with open(input_file) as f:
        reader=csv.reader(f)
        for row in reader:
            print(row)

