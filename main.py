import geneID_dict
import calculate_FST_avg as cfa
import random_fst_test as rft
import sys
import argparse
import os


parser = argparse.ArgumentParser(description='Run CatPop on a category assignment file and a fst file. Generate a prefix for both, and have the \n files be formatted as <inputprefix_fst.csv> and <inputprefix_categories.csv>')
parser.add_argument('-i', "--input_prefix", help='The prefix of the files you wish to use.')
args = parser.parse_args()

fst_in = args.input_prefix + "_fst.csv"
cat_in = args.input_prefix + "_categories.csv"

if not (os.path.exists(fst_in) and os.path.exists(cat_in)):
    print(f"Error: Input files '{fst_in}' and '{cat_in}' do not exist")
    sys.exit(1)

# Allows users to type in names of files in command line
if len(sys.argv) < 2:
    print("Usage: python3 main.py <input_prefix>")
    sys.exit(1)


#rft.make_fst_file(8, 547)
print('Hello! Your results are being calculated')
cfa.identify_significant_loci(fst_in, cat_in)

