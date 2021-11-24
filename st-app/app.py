##__all__ = ['DATA_INFO', 'AUTHOR_INFO', 'APP_NAME', 
##            'SideBar', 'app_sidebar', 'IMAGE_PATH', 
##           'load_cached_data', 'app_mainscreen', 'sb']

import numpy as np
import pandas as pd
import datetime as dt
import csv

from pathlib import Path
import streamlit as st
from xml.etree import ElementTree as et

from PIL import Image
from IPython.display import display

from databooth.convert_data import set_local_or_remote_data_path, convert_csv_row_to_xml

from databooth.parse_tcx import get_tcx_lap_data, get_tcx_point_data, get_dataframes

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

DATAFILE_PATH = "data"
DATAFILE_CSV  = "2021_09_26_17_09_Chamonix_Ride_Part_1,_France.csv"
DATAFILE_URL_PATH = "https://raw.githubusercontent.com/DataBooth/client-youngm-ifit/main/data/" 
DATAFILE_URL = DATAFILE_URL_PATH + DATAFILE_CSV.replace(",", "%2C")

#def ST_APP_CONFIG_TOML = Path().cwd().parent / \"app_secrets.toml\" - TODO: TT to refactor
class SideBar:
    app_name = APP_NAME
    client_name = CLIENT_NAME
    datasource = DATA_INFO
    author = AUTHOR_INFO
    data_title = 'Data details...'
    data_local = False
    file_name = "Select CSV file..."


def app_sidebar(APP_NAME):
    sb = SideBar()
    st.sidebar.info("Menu")
    st.sidebar.image(image=IFIT_BRAND_URL, use_column_width=True, output_format='PNG')
    st.sidebar.markdown(sb.author)
    return sb


# @st.cache
def load_and_cache_data():
    data_df = pd.read_feather(CACHED_DATA)   # load cached (downsampled) data
    return data_df


#def convert_xml_to_dataframe(xml_str, df_cols, tag="data"):
    #st.write(xml_str)
#    etree = et.fromstring(xml_str)
#    eroot = etree.getroot() 
#    st.write(eroot)
#    df = pd.DataFrame(columns=df_cols)
#    for i in etree.iter(tag=tag):
#        df = df.append(
#            pd.Series([i.get(df_cols[0]), i.get(df_cols[1])], index=dfcols),
#            ignore_index=True)
#    return df

    import jxmlease

def test_easyxml():
    myparser = jxmlease.Parser()
    root = myparser("<a>foo</a>")
    st.write(root)
    return root


def app_mainscreen(APP_NAME, sb):
    st.header(APP_NAME + " // " + CLIENT_NAME)

    root = test_easyxml()

    if sb.data_local == True:
        csv_file_name = st.file_uploader("Name of CSV data file to convert?", type=['csv'])

    # IMPORT TCX
        tcx_file_name = st.file_uploader("Name of TCX data file you would like to merge", type = ['tcx'])
        new_tcx = ''.join(data_df.apply(convert_csv_row_to_xml, axis=1))
    
    else:
        DATASOURCE_TYPE = "gh"
        csv_file_name, tcx_file_name = set_local_or_remote_data_path(DATASOURCE_TYPE, DATAFILE_PATH, DATAFILE_CSV, DATAFILE_URL)
        st.write("CSV: " + csv_file_name)
        st.write("TCX: " + tcx_file_name)
    # CONVERT TCX to CSV - instead let's just make tcx into a pandas data frame

    # import data
    data_df = pd.DataFrame()

    if csv_file_name is not None:
        data_df = pd.read_csv(csv_file_name, skiprows=2)

    data_df.rename(columns={"Relative Resistance": "RelativeResistance"}, inplace=True)

    show_raw_csv = st.checkbox("Show raw CSV data")
    if show_raw_csv:
        st.write(data_df)

    if tcx_file_name is not None:
        # st.write(tcx_file_name)
        #tmp = pd.read_xml(tcx_file_name)
        #st.write(pd.__version__)
        
        # if it is a file
        #with open(tcx_file_name) as f:
        #    xml_str = f.readlines()

    # if it is a URL
        import requests

        response = requests.get(tcx_file_name)
        xml_str = response.text

        df_cols = ["DistanceMeters", "Cadence"]

        df_xml = convert_xml_to_dataframe(xml_str, df_cols, tag="data")
        st.write(df_xml)

        try:    
            #xtree = et.parse(tcx_file_name)
            xroot = xtree.getroot() 

            df_cols = ["DistanceMeters", "Cadence", "Calories", "HeartRateBPM", "Time", "AltitudeMeters", "LongitudeDegrees", "LatitudeDegrees"]
            rows = []

            for node in xroot: 
                DistanceMeters = node.find("DistanceMeters").text if node is not None else None
                Cadence = node.find("Cadence").text if node is not None else None
                Calories = node.find("Calories").text if node is not None else None
                HeartRateBPM = node.find("HeartRateBPM").text if node is not None else None
                Time = node.attrib.get("Time").text if node is not None else None
                AltitudeMeters = node.find("AltitudeMeters").text if node is not None else None
                LongitudeDegrees = node.find("LongitudeDegrees").text if node is not None else None
                LatitudeDegrees = node.find("LatitudeDegrees").text if node is not None else None
                
                rows.append({"DistanceMeters": DistanceMeters, "Cadence": Cadence, 
                            "Calories": Calories, "HeartRateBPM": HeartRateBPM,
                            "Time": Time, "AltitudeMeters": AltitudeMeters, 
                            "LongitudeDegrees": LongitudeDegrees, "LatitudeDegrees": LatitudeDegrees})

            tcx_df = pd.DataFrame(rows, columns = df_cols)

            show_raw_xml = st.checkbox("Show raw XML data")
            if show_raw_xml:
                st.write(tcx_df)

        except Exception as e:
            st.write(e)


    # merging the two
    # have to figure out a way to minus time 0 from time 1 in the tcx file - it just comes out as the time and seconds
    # pd.merge(tcx_df, data_df, on = "Time")

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
