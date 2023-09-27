import geneID_dict
import calculate_FST_avg as cfa
import random_fst_test as rft
import sys
import argparse

parser = argparse.ArgumentParser(description='Run CatPop on selected files')
parser.add_argument('input_fst_file', help='The input file with the previously calculated fsts, correctly formatted.')
parser.add_argument('input_category_assignments_file', help='The input file with correctly formatted category assignments')
args = parser.parse_args()

#Need to make this so that it only in one name, like so:
# python3 main.py -i Hu_2021_orchids


# Developing the following method:
def example_function(x): #deleting later
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, 'i:', ['foperand'])
        if len(opts) == 0 and len(opts) >1:
            print("Usage: main.py -i <input_file_prefix>")
        else:
            for opt, arg in opts:
            # Enter script to run here

    except getopt.GetoptError:
        print("Usage: python3 main.py -i <input_file_prefix>")
        sys.exit(1)


# Allows users to type in names of files in command line
if len(sys.argv) < 3:
    print("Usage: python3 main.py <input_fst_file> <input_category_assignments_file>")
    sys.exit(1)

input_fst_file=sys.argv[1]
input_cat_assn_file = sys.argv[2]


rft.make_fst_file(8, 547)
print('Hello!')
cfa.identify_significant_loci(input_fst_file, input_cat_assn_file)

#cfa.identify_significant_loci("random_fst_test.csv", "CategoryAssignments_test.csv")
#cfa.identify_significant_loci("Hu_2021_orchids_fst.csv", "Hu_2021_orchids_categories.csv")

