# PopCat Combinatorics

This software package uses combinatorics to create all possible scenarios of two
population assignments, performs a permutation test for each comparison, and
generates a p-value distribution plot, along with graphs that show the association of between/within
ecotype comparisons, and additionally returns the genes of significance.

There is also a number generator to ensure the accuracy of your data

# Contents
* Flow of data and Outputs
* Instructions to implement your comparisons
* Other information
# Flow of Data

Please refer to the image below to understand the flow of data through the
program.
![Data Flow](data_flow.png)

The outputs of this program is as follows:

* p-value plot
* Ecotype comparison of within and between plot
* results.txt, which will list all the genes and their related p-values
* log.txt, which will contain all the genes with a p-value below .05
/* sig_output.csv shows the significant genes
* all_output.csv reports every delta_fst and p-values for the genes

# Instructions to Implement your Comparisons
This program takes in two files as input. Your input files need a "_categories.csv" and a "_fst.csv" suffix,
according to their filetype. In your categories file, the columns need to be labelled with the
underscore between the population names. Comparisons with non-numeric fst values will be ignored.
Also, assign your True scenarios in your "categories.csv".

# Running CatPop


* install python
* open terminal and navigate to CatPop directory
* type the following and review results
```
python main.py -i <input_file_prefix>
```
* You will see a message when finished that shows you the names of the output
  files.
# Other Information
If you get an error saying "Fst_Pop1_Pop2 and Fst_Pop2_Pop1 not found, check your input files and verify that the populations are spelled exactly the same in the fst and ecotype files.

