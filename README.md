# Clustermap-generator
## Description
This python code creates an UPGMA-based clustermap, with clustering in columns. Optional normalisation, sorting, removing columns, title adding, operated by constants declared in lines 7-14.
## Libraries required
Pandas, sys, matplotlib.plot, seaborn
## Usage instructions
When running the code, provide an argument (=path to the .csv) in the terminal. 
### Do note: 
* The basic delimiter is ";", declared in line 7; change to other (e.g. ",") if needed.
* The code assumes the data is provided in columns, not in rows!
