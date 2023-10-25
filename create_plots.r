# Load the optparse package
library(optparse)
# Define the command-line args
option_list = list(
  make_option(c("-i", "--input"), type = "character", help = "Input CSV file, with <input_prefix>_all_outputs.csv"),
  make_option(c("-d", "--directory"), type = "character", help "Set working directory where CatPop located"),
  make_option(c("-o", "--output"), type = "character", help = "Output PDF file"),
  make_option(c("-p", "--pvalue"), type = "numeric", default = 0.05, help = "P-value threshold for vertical line"),
  make_option(c("-b", "--bins"), type = "integer", default = 50, help = "Number of bins for histogram")
)
# Parse command line arguments
opt_parser = OptionParser(usage = "R create_plots.R [options]", option_list = option_list)
opt = parse_args(opt_parser)

setwd(opt$directory)
# path MUST be in quotes
dat <- read.csv(opt$input)
# file MUST be in quotes
# imports data as dataframe with heading

# look at all geneIDs
dat$GeneID
# look at all p-values
dat$P.value

# using ggplot2, create density chart
# if you don't have ggplot2 package installed, you'll  need to do so as follows:
#install.packages('ggplot2')
# if you already have it installed, just load it
library(ggplot2)

# plot your data! Assign the plot to a variable called 'density_plot'
density_plot = ggplot(dat, aes(x=P.value)) + geom_vline(xintercept= opt$pvalue, linetype="dashed", size = 1, color = "#F68A8A") + geom_histogram(color="black" , fill="white", bins opt$bins)
# check out your plot and save it write your plot to a file:
pdf("opt$output")
density_plot
dev.off()

# For this section you will use a few other R packages
library(reshape2)
library(tidyverse)

dat_melted <- reshape2::melt(dat, id.vars = c("GeneID", "P.value", "Significant"), measure.vars=c("TrueDeltaSame", "TrueDeltaDiff"))
dat_melted$ordered_var <- with(dat_melted, relevel(variable, "TrueDeltaSame"))
dat_melted <- dat_melted[order(dat_melted$Significant),]

fst_exons_Plot <- dat_melted %>%
  ggplot(aes(x=ordered_var,y=value), axis.line = element_line(colour = 'black', linewidth= 3)) +
  theme_classic(base_size = 25) +
  geom_boxplot(lwd=1, fatten=2, outlier.shape=NA, aes(colour="black"), show.legend = F, alpha=0) +
  geom_line(size=1, aes(group=GeneID, linetype=Significant, colour = Significant, alpha=Significant), position = position_dodge(0.2), show.legend = F) +
  scale_linetype_manual(values=c("no" = "dotted","yes" = "solid")) +
  scale_color_manual(values=c("no" = "#4B4B4B", "yes" = "#e6b002")) +
  geom_point(aes(fill=variable,group=GeneID,colour=factor(Significant), alpha=Significant), position = position_dodge(0.2), size = 3, show.legend = F) +
  scale_x_discrete(labels=c("Within", "Between")) +
  xlab('Comparison Type') + ylab('fst') + # geom_text(aes(label=GeneID), size = 2) +
  geom_hline(yintercept=0.02, linetype="dashed", size = 1, color = "#F68A8A")
  theme(legend.position = "top")
fst_exons_Plot
