# CatPop Combinatorics

This software package uses combinatorics to create all possible scenarios of two
population assignments, performs a permutation test for each comparison, and
generates a p-value distribution plot, along with graphs that show the association of between/within
ecotype comparisons, and additionally returns the genes of significance.

There is also a number generator to ensure the accuracy of your data

# Contents
* Flow of data and Outputs
* Instructions to implement your comparisons
* Other information

# Instructions to Implement your Comparisons
### Step 1: Cloning the Repository
1. Ensure you have git installed. Instructions on installing git can be found
[here](https://git-scm.com/downloads)
2. Open your terminal and navigate to the directory you wish to put the
   repository. This would look something like ```cd ~/GitHubRepositories```
3. Assuming you are reading this, you are on the page of the repository. Scroll up to click on the green clone button and copy
   the repository's URL for cloning. Then, on your terminal, use the command:
   ```
   git clone <repository URL>
   ```
4. Git then downloads the entire repository to your local device.  You'll see
   progress information as the cloning takes place.
5. Once cloning is complete, you'll have a copy of the repository on your local
   machine in the subdirectory with the same name as the repository. You now
   should navigate into this directory to use functions this repository has.

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

The outputs of this program is as follows:

* p-value plot
* Ecotype comparison of within and between plot
* results.txt, which will list all the genes and their related p-values
* log.txt, which will contain all the genes with a p-value below .05
/* sig_output.csv shows the significant genes
* all_output.csv reports every delta_fst and p-values for the genes
# Other Information
If you get an error saying "Fst_Pop1_Pop2 and Fst_Pop2_Pop1 not found, check your input files and verify that the populations are spelled exactly the same in the fst and ecotype files.

# Flow of Data

Please refer to the image below to understand the flow of data through the
program.
![Data Flow](data_flow.png)
