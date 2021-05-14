import sys

import pandas as pd

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print("biopan_csv.py inputfile outputfile")
        exit(1)
    input_file= sys.argv[1]
    output_file=sys.argv[2]


    
    df=pd.read_csv(input_file)
    cols_to_drop = [1,2,3,4]
    new_df=df.drop(df.columns[cols_to_drop],axis=1)

    new_df.to_csv(output_file,index=False)
                

