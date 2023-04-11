setwd(insert-path-to-repository)
# path MUST be in quotes
dat <- read.csv('all_output.csv')
# file MUST be in quotes
# imports data as dataframe with heading

# look at all geneIDs
dat$GeneID
# look at all p-values
dat$P.value

# using ggplot2, create density chart
# if you don't have ggplot2 package installed, you'll  need to do so as follows:
install.packages('ggplot2')
# if you already have it installed, just load it
library(ggplot2)
# plot your data! Assign the plot to a variable called 'density_plot'
density_plot = ggplot(dat, aes(x=P.value)) + geom_histogram(color="black", fill="white", bins=50)
# check out your plot and save it write your plot to a file:
pdf("density_plot.pdf")
density_plot
dev.off()
