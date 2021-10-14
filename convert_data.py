import pandas as pd

# 1 - Read CSV
# 2 - Convert CSV to XML file
# 3 - join the two files together


# How to read csv
csv_df = pd.read_csv("sassafras.csv", skiprows=2)
print(csv_df.head())

# How to read xml
#xml_data = open('tcxfile.tcx', 'r').read()
#print(xml_data)


# Convert CSV to XML

def convert_row(row):
    return """<Time>%s</Time>
    <Miles>%s</Miles>
    <MPH>%s</MPH>
    <Watts>%s</Watts>
    <HR>%s</HR>
    <RPM>%s</RPM>
    <Resistance>%s</Resistance>
    <Relative Resistance>%s</Relative Resistance>
    <Incline>%s</Incline>""" % (row.Time, row.Miles, row.MPH, row.Watts, row.HR, row.RPM, row.Resistance, row.RelativeResistance, row.Incline)

# issue is I have to change "Relative Resistance" to "RelativeResistance" for the above code to work.

newtcx = '\n'.join(csv_df.apply(convert_row, axis=1))

# print(newtcx)

# Join modified XML file to original TCX file
with open("sassafras.tcx", "a") as tcxwrite: 
  for line in newtcx:
    tcxwrite.write(line)


# REFERENCES
# https://towardsdatascience.com/the-easy-way-to-work-with-csv-json-and-xml-in-python-5056f9325ca9
# https://stackabuse.com/reading-and-writing-xml-files-in-python-with-pandas/
# https://roytuts.com/how-to-convert-csv-to-xml-using-python/
# https://stackoverflow.com/questions/41059264/simple-csv-to-xml-conversion-python
