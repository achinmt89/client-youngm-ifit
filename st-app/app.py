##__all__ = ['DATA_INFO', 'AUTHOR_INFO', 'APP_NAME', 
##            'SideBar', 'app_sidebar', 'IMAGE_PATH', 
##           'load_cached_data', 'app_mainscreen', 'sb']

import numpy as np
import pandas as pd
import datetime as dt

from pathlib import Path
import streamlit as st

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

st.set_page_config(page_title=APP_NAME, layout='wide')

IMAGE_PATH = 'st-app/resources'
IMAGE_PATH = Path.cwd().resolve()/IMAGE_PATH

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

class SideBar:
    app_name = APP_NAME
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
    st.sidebar.info(APP_NAME + ": Menu")
    col1, col2 = st.sidebar.beta_columns(2)

    with col1:
        st.write(IMAGE_PATH)
        #mage1 = Image.open(IMAGE_PATH/'AppleWatchExercise.jpeg').resize((144, 144))  # NOTE: resize done here
        #st.image(image=image1, use_column_width=True, output_format='JPEG')
    with col2:
        st.markdown("## TODO")
        #image2 = Image.open(IMAGE_PATH/'HealthFitLogo.png')
        #st.image(image=image2, use_column_width=True, output_format='PNG')

    st.sidebar.markdown(sb.author)

    return sb


# @st.cache
def load_and_cache_data():
    data_df = pd.read_feather(CACHED_DATA)   # load cached (downsampled) data
    return data_df


def app_mainscreen(APP_NAME, sb):
    st.header(APP_NAME)
    st.write("Today's date: " + str(sb.today_date))
    st.write()
    csv_file_name = st.file_uploader("Name of CSV data file to convert?")

    # import data
    data_df = pd.read_csv(csv_file_name, skiprows=2)
    data_df.rename(columns={"Relative Resistance": "RelativeResistance"}, inplace=True)
    
    new_tcx = ''.join(data_df.apply(convert_csv_row_to_xml, axis=1))
    
#    data_df = load_cached_walking_data()
#    sb.datasize = data_df.memory_usage(deep=True).sum() / 1024 / 1024

    show_raw = st.checkbox("Show raw data")
    if show_raw:
        st.write(data_df)
        st.write(new_tcx)

#    return data_df
    return csv_file_name
    

sb = app_sidebar(APP_NAME)

app_mainscreen(APP_NAME, sb)
