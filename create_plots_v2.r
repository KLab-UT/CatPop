# Set working directory to your repository path (insert the correct path within quotes)
setwd("insert-path-to-repository")

# Import data from 'all_output.csv' into a dataframe
dat <- read.csv('all_output.csv')

# Display GeneID column
dat$GeneID

# Display P-value column
dat$P.value

# Load the ggplot2 package or install it if not already installed
# Install ggplot2 if needed: install.packages('ggplot2')
library(ggplot2)

# Create a density chart using ggplot2
density_plot <- ggplot(dat, aes(x=P.value)) +
      geom_vline(xintercept=0.05, linetype="dashed", size=1, color="#F68A8A") +
        geom_histogram(color="black", fill="20") +
          labs(x="P-value") + # Add labels
            theme_minimal() # Customize the plot's theme

# Save the plot to a PDF file
pdf("density_plot.pdf")
print(density_plot)
dev.off()

# Load necessary R packages
library(reshape2)
library(tidyverse)

# Reshape the data for visualization
dat_melted <- reshape2::melt(dat, id.vars=c("GeneID", "P.value", "Significant"), measure.vars=c("TrueDeltaSame", "TrueDeltaDiff"))
dat_melted$ordered_var <- with(dat_melted, relevel(variable, "TrueDeltaSame"))
dat_melted <- dat_melted[order(dat_melted$Significant),]

# Create a boxplot and line plot
fst_exons_Plot <- dat_melted %>%
      ggplot(aes(x=ordered_var, y=value)) +
        geom_boxplot(lwd=1, fatten=2, outlier.shape=NA, aes(colour="black"), show.legend=FALSE, alpha=0) +
          geom_line(size=1, aes(group=GeneID, linetype=Significant, colour=Significant, alpha=Significant), position=position_dodge(0.2), show.legend=FALSE) +
            scale_linetype_manual(values=c("no"="dotted", "yes"="solid")) +
              scale_color_manual(values=c("no"="#4B4B4B", "yes"="#e6b002")) +
                geom_point(aes(fill=variable, group=GeneID, colour=factor(Significant), alpha=Significant), position=position_dodge(0.2), size=3, show.legend=FALSE) +
                  scale_x_discrete(labels=c("Within", "Between")) +
                    xlab('Comparison Type') + ylab('fst') +
                      geom_hline(yintercept=0.02, linetype="dashed", size=1, color="#F68A8A") +
                        theme(legend.position="top", axis.line=element_line(colour='black', linewidth=3), base_size=25)

                    fst_exons_Plot

