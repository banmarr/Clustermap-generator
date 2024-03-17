import pandas as pd
import sys as sys
import matplotlib.pyplot as plt
import seaborn as sns

#declare constants (name of column to sort by, direction of sorting (ascending = True and descending = False), which columns to remove, which column to use as index (by index), whether to standardize the data in columns, whether to assign title to the chart (True - use, False - don't use), what the title should be)
SEPARATOR = ";"
SORTBY = "76GS"
DIRECTION = True
HIDE = ['76GS', 'EMT class 76GS-based','KS','EMT class KS-based']
INDEX = 0
NORMALISE = True
USETITLE = False
TITLE = "Gene expression in basal breast cancer cell lines"

#check if argument (.csv with expression statistics and phenotype classes) present
if len(sys.argv) != 2:
    raise Exception("No argument provided!")

#load argument as pandas table
path = str(sys.argv[1])
df = pd.read_csv(path, sep=SEPARATOR, header = 0, index_col = INDEX)

#sort by SORTBY column (don't sort if SORTBY = None)
if SORTBY != None:
    sorted_df = df.sort_values(by=[SORTBY], ascending=DIRECTION)
else:
    sorted_df = df #will be called sorted even if no sorting took place!

#remove columns specified in HIDE (don't remove if HIDE = None or HIDE == [])
if HIDE != None and HIDE != []:
     final_df = sorted_df.drop(columns=HIDE)
else:
    final_df = sorted_df

#create heatmap with clustering (UPGMA)
if NORMALISE == True:
    result = sns.clustermap(final_df, row_cluster = False, cmap='coolwarm', z_score = 1, annot=True, xticklabels=True, yticklabels=True, annot_kws={"fontsize":6})
else:
    result = sns.clustermap(final_df, row_cluster = False, cmap='coolwarm', annot=True, xticklabels=True, yticklabels=True, annot_kws={"fontsize":6})

#add title
if USETITLE == True and TITLE != None:
    result.figure.suptitle(TITLE)

#show clustermap
plt.show()
