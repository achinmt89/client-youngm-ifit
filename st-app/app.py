##__all__ = ['DATA_INFO', 'AUTHOR_INFO', 'APP_NAME', 'CACHED_WALK_DATA', 'plot_walk', 'plot_entire_walk',
##           'plot_walk_points', 'SideBar', 'app_sidebar', 'IMAGE_PATH', 'IMAGE_PATH', 'WALK_NAME', 'WALK_NAME',
##           'load_cached_walking_data', 'app_mainscreen', 'notebook_mainscreen', 'sb']

# Cell

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


DATA_INFO = 'TODO'
AUTHOR_INFO = 'TODO'
APP_NAME = 'TODO'
CACHED_WALK_DATA = 'TODO'

st.set_page_config(page_title=APP_NAME, layout='wide')

# IMAGE_PATH = 'emmaus_walking/resources'
# IMAGE_PATH = Path.cwd().resolve()/IMAGE_PATH

class SideBar:
    datasource = DATA_INFO
    datasize = 0   # TODO: Look to calculate this (in GB)
    author = AUTHOR_INFO
    data_title = 'Data details...'
    data_local = False
    today_date = dt.date.today()
#   end_date = dt.date.today()
#    selected_data = None


def app_sidebar(APP_NAME):

    sb = SideBar()

    st.sidebar.info(APP_NAME)

    col1, col2 = st.sidebar.beta_columns(2)

    with col1:
#        image1 = Image.open(IMAGE_PATH/'AppleWatchExercise.jpeg').resize((144, 144))  # NOTE: resize done here
#        st.image(image=image1, use_column_width=True, output_format='JPEG')
    with col2:
#        image2 = Image.open(IMAGE_PATH/'HealthFitLogo.png')
#        st.image(image=image2, use_column_width=True, output_format='PNG')

    st.sidebar.markdown(sb.author)
    sb.file_name = st.sidebar.file_uploader()

    return sb



# @st.cache
def load_and_cache_data():
    data_df = pd.read_feather(CACHED_DATA)   # load cached (downsampled) data
    return data_df


def app_mainscreen(APP_NAME, sb):

    st.header(sb.file_name)
    data_df = load_cached_walking_data()
    sb.datasize = data_df.memory_usage(deep=True).sum() / 1024 / 1024

    return data_df
