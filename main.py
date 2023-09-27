import geneID_dict
import calculate_FST_avg as cfa
import random_fst_test as rft
import sys
import argparse

parser = argparse.ArgumentParser(description='Run CatPop on selected files')
parser.add_argument('--input_prefix', "-i", help='The input file with the previously calculated fsts, correctly formatted.')
args = parser.parse_args()

fst_in = args.input_prefix + "_fst.csv"
cat_in = args.input_prefix + "_categories.csv"

# Allows users to type in names of files in command line
if len(sys.argv) < 2:
    print("Usage: python3 main.py <input_prefix>") 
    sys.exit(1)


#rft.make_fst_file(8, 547)
print('Hello!')
cfa.identify_significant_loci(fst_in, cat_in)

