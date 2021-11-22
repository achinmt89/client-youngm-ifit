# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython #AChin: Want to avoid use of this probs in non-notebook

# %% [markdown]
# ## Convert Mick's movement data
# 
# 1. Read CSV
# 2. Convert CSV to XML file
# 3. Join the two files together

# %%
#!pip install pandas


# %%
import pandas as pd
from pathlib import Path


# %%
# DATASOURCE_TYPE = "local"  # Local machine
DATASOURCE_TYPE = "gh"     # Github - Synthetic or non-PII data only

#TODO: Need to check that both local and remote (in this instance Github.com) data modes work


# %%
DATAFILE_PATH = "data"
DATAFILE_CSV  = "2021_09_10_15_09_Sassafras_Power_Climb,_Sunset,_South_Carolina.csv"

# DATAFILE_URL = "https://raw.githubusercontent.com/DataBooth/client-youngm-ifit/main/data/" + "2021_09_10_15_09_Sassafras_Power_Climb%2C_Sunset%2C_South_Carolina.csv"

DATAFILE_URL_PATH = "https://raw.githubusercontent.com/DataBooth/client-youngm-ifit/main/data/" 
DATAFILE_URL = DATAFILE_URL_PATH + DATAFILE_CSV.replace(",", "%2C")


# %%
# print(DATAFILE_URL)


# %%
def set_local_or_remote_data_path(datasource_type, datafile_path, datafile_csv, datafile_url):
  if datasource_type ==  "local":
    datafile = Path(datafile_path) / datafile_csv
    print("Local datasource: " + datafile.as_posix())
    tcxfile = Path(datafile_path) / datafile_csv.replace("csv", "tcx")
    print("TCX file to be created: " + tcxfile.as_posix())
    return datafile, tcxfile
  elif datasource_type == "gh":
    datafile = datafile_url
    print("Remote datasource: " + datafile)
    tcxfile = datafile.replace("csv", "tcx")
    print("TCX file to be created: " + tcxfile)
    return datafile, tcxfile
  else:
    print("ERROR: Unknown `datasource_type`")
  return None

  #TODO: Aaron - we can refactor further 


# %%
datafile, tcxfile = set_local_or_remote_data_path(DATASOURCE_TYPE, DATAFILE_PATH, DATAFILE_CSV, DATAFILE_URL)


# %%
# DATAFILE

#TODO: Aaron we can re-factor this together if you'd like 


# %%
#!head $DATAFILE


# %%
# How to read csv

data_df = pd.read_csv(datafile, skiprows=2)
print(data_df.head())

# How to read xml
# xml_data = open('tcxfile.tcx', 'r').read()
# print(xml_data)


# %%
data_df.rename(columns={"Relative Resistance": "RelativeResistance"}, inplace=True)


# %%
# TODO: Aaron to read about self-documenting code 

def convert_csv_row_to_xml(row):
    return """<Time>%s</Time>
    <Miles>%s</Miles>
    <MPH>%s</MPH>
    <Watts>%s</Watts>
    <HR>%s</HR>
    <RPM>%s</RPM>
    <Resistance>%s</Resistance>
    <Relative Resistance>%s</Relative Resistance>
    <Incline>%s</Incline>""" % (row.Time, row.Miles, row.MPH, row.Watts, row.HR, row.RPM, row.Resistance, row.RelativeResistance, row.Incline)

# TODO: The issue I currently have is how to change "Relative Resistance" to "RelativeResistance" for the above code to work


# %%
new_tcx = ''.join(data_df.apply(convert_csv_row_to_xml, axis=1))


# %%
#data_df


# %%
# Join modified XML file to original TCX file


# TCXFILE = Path(DATAFILE_PATH) / DATAFILE_CSV.replace("csv", "tcx") - see above


# %%
#with open(tcxfile, "a+") as tcxwrite: 
#  for line in new_tcx:
#    tcxwrite.write(line)


# %%
#!tail -40 $TCXFILE - convert to actual .py code for compatibility between notebook & script

# get_ipython().system('tail -40 ' + tcxfile)

# %% [markdown]
# ## References
# 
# * https://towardsdatascience.com/the-easy-way-to-work-with-csv-json-and-xml-in-python-5056f9325ca9
# * https://stackabuse.com/reading-and-writing-xml-files-in-python-with-pandas/
# * https://roytuts.com/how-to-convert-csv-to-xml-using-python/
# * https://stackoverflow.com/questions/41059264/simple-csv-to-xml-conversion-python

