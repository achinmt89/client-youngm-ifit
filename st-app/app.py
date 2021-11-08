##__all__ = ['DATA_INFO', 'AUTHOR_INFO', 'APP_NAME', 
##            'SideBar', 'app_sidebar', 'IMAGE_PATH', 
##           'load_cached_data', 'app_mainscreen', 'sb']

import numpy as np
import pandas as pd
import datetime as dt
import csv

from pathlib import Path
import streamlit as st
from xml.etree import ElementTree

from PIL import Image
from IPython.display import display

# TODO: Following is a hack to fix issue with import paths using in notebook vs. script

# try:
#     from .datapipe import load_and_cache_raw_data
# except:
#    from datapipe import load_and_cache_raw_data

# TODO: Link in read .toml config & secrets

DATA_INFO = 'Supplied by Client (YoungM)'
AUTHOR_INFO = 'Aaron Chin @ DataBooth.com.au'
APP_NAME = "iFit Data Conversion app"
CACHED_DATA = 'TODO: Data cache file'
CLIENT_NAME = 'Mick Young'

st.set_page_config(page_title=APP_NAME, layout='wide')

AVATAR_URL = "https://www.w3schools.com/howto/img_avatar.png"
IFIT_BRAND_URL = "https://images.contentstack.io/v3/assets/blt1d89a78b502b83f3/blt000cfbfbc534f253/615468f7c3934450a14e3233/img_bikes_hero_dsk.jpg?q=90"
#IMAGE_PATH = 'st-app/resources'
#IMAGE_PATH = Path.cwd().resolve()/IMAGE_PATH

#def ST_APP_CONFIG_TOML = Path().cwd().parent / \"app_secrets.toml\"

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

class SideBar:
    app_name = APP_NAME
    client_name = CLIENT_NAME
    datasource = DATA_INFO
    datasize = 0   # TODO: Look to calculate this (in GB)
    author = AUTHOR_INFO
    data_title = 'Data details...'
    data_local = False
    today_date = dt.date.today()
    file_name = "Select CSV file..."
#   end_date = dt.date.today()
#    selected_data = None


def app_sidebar(APP_NAME):
    sb = SideBar()
    st.sidebar.info("Menu")
    # col1, col2 = st.sidebar.beta_columns(2)

    #with col1:
        #st.write(IMAGE_URL)
        #mage1 = Image.open(IMAGE_PATH/'AppleWatchExercise.jpeg').resize((144, 144))  # NOTE: resize done here
    st.sidebar.image(image=IFIT_BRAND_URL, use_column_width=True, output_format='PNG')
    #with col2:
        #st.markdown("## TODO")
        #image2 = Image.open(IMAGE_PATH/'HealthFitLogo.png')
        #st.image(image=image2, use_column_width=True, output_format='PNG')

    st.sidebar.markdown(sb.author)

    return sb


# @st.cache
def load_and_cache_data():
    data_df = pd.read_feather(CACHED_DATA)   # load cached (downsampled) data
    return data_df


def app_mainscreen(APP_NAME, sb):
    st.header(APP_NAME + " // " + CLIENT_NAME)
    #st.write("Today's date: " + str(sb.today_date))
    #st.file_uploader
    csv_file_name = st.file_uploader("Name of CSV data file to convert?", type=['csv'])
    
    # st.write(csv_file_name)
    
    # import data
    data_df = pd.DataFrame()

    if csv_file_name is not None:
        data_df = pd.read_csv(csv_file_name, skiprows=2)

    
    data_df.rename(columns={"Relative Resistance": "RelativeResistance"}, inplace=True)

    tcx_file_name = st.file_uploader("Name of TCX data file you would like to merge", type = ['tcx'])

    new_tcx = ''.join(data_df.apply(convert_csv_row_to_xml, axis=1))
    
    #data_df = load_cached_walking_data()
    #sb.datasize = data_df.memory_usage(deep=True).sum() / 1024 / 1024
    
    # CONVERT TCX to CSV
    tree = ElementTree.parse(tcx_file_name)

    output_tcx = open(tcx_file_name, w, newline = '', encoding= 'utf-8')
    csv_writer = csv.writer(tcx_file_name)

    col_names = ['DistanceMeters', 'Cadence', 'Calories', 'HeartRateBPM', 'Time', 'AltitudeMeters', 'LongitudeDegrees', 'LatitudeDegrees']
    csvwriter.writerow(col_names)
    #rows = []

    root = tree.getroot()

    for eventData in root.findall('eventData'):
        event_data = []
        event = eventData.find('event')

        DistanceMeters = event.find("DistanceMeters")
        if DistanceMeters != None:
            DistanceMeters = DistanceMeters.text
        event_data.append(DistanceMeters)

        Cadence = event.find("Cadence")
        if Cadence != None:
            Cadence = Cadence.text
        event_data.append(Cadence)

        Calories = event.find("Calories")
        if Calories != None:
            Calories = Calories.text
        event_data.append(Calories)

        HeartRateBPM = event.find("HeartRateBPM")
        if HeartRateBPM != None:
            HeartRateBPM = HeartRateBPM.text
        event_data.append(HeartRateBPM)

        Time = event.find("Time")
        if Time != None:
            Time = Time.text
        event_data.append(Time)

        AltitudeMeters = event.find("AltitudeMeters")
        if AltitudeMeters != None:
            AltitudeMeters = AltitudeMeters.text
        event_data.append(AltitudeMeters)

        LongitudeDegrees = event.find("LongitudeDegrees")
        if LongitudeDegrees != None:
            LongitudeDegrees = LongitudeDegrees.text
        event_data.append(LongitudeDegrees)

        LatitudeDegrees = event.find("LatitudeDegrees")
        if LatitudeDegrees != None:
            LatitudeDegrees = LatitudeDegrees.text
        event_data.append(LatitudeDegrees)

        csvwriter.writerow(event_data)

    output_csv.close()

    csv_df = pd.read_csv(tcx_file_name)

        #rows.append({"DistanceMeters":DistanceMeters,
        #"Cadence": Cadence,
        #"Calories": Calories,
        #"HeartRateBPM": HeartRateBPM,
        #"Time": Time,
        #"AltitudeMeters": AltitudeMeters,
        #"LongitudeDegrees": LongitudeDegrees,
        #"LatitudeDegrees": LatitudeDegrees})

   # df = pd.DataFrame(rows, col_names)

    df.to_csv('output.csv')

    # joining tcx
    #TCXFILE = pd.read_xml(tcx_file_name)

    #with open(TCXFILE, "a") as tcxwrite: 
        #for line in new_tcx:
            #tcxwrite.write(line)
            
    show_raw_csv = st.checkbox("Show raw CSV data")
    if show_raw_csv:
        st.write(data_df)
        #st.write(new_tcx)
        #st.write(TCXFILE)

    show_raw_xml = st.checkbox("Show raw XML data")
    if show_raw_xml:
        st.write(new_tcx)

    # return data_df
    return csv_file_name

sb = app_sidebar(APP_NAME)

app_mainscreen(APP_NAME, sb)

# TODO: display XML bug?
# TODO: join tcx to csv on date/time?
# TODO: define testing
# TODO: do testing
# TODO: complete documentation
# TODO: refactor and retest


# https://medium.com/analytics-vidhya/converting-xml-data-to-csv-format-using-python-3ea09fa18d38
# https://www.geeksforgeeks.org/convert-xml-to-csv-in-python/
