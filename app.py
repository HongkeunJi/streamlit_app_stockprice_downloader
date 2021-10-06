import streamlit as st
from utils.utils import read_json, download_df
from utils.utils_fdr import get_comp_info, get_stock_data
import time


@st.cache(suppress_st_warning=True, show_spinner=False)
def load_comp_list():
    stock_const = read_json('resource/stock_list.json')
    return stock_const


def get_target_comp_info(comp_info_all: dict):

    col1, col2 = st.columns([3, 3])
    country = col1.radio("Select country", comp_info_all.keys())
    market = col2.radio("Select market", comp_info_all[country].keys())
    company = st.selectbox('Select company', comp_info_all[country][market].keys())
    comp_info = comp_info_all[country][market][company]

    return comp_info

def main():
    st.title("Stockprice Data Downloader")
    stock_list = load_comp_list()

    comp_info = get_target_comp_info(stock_list)
    num_month = st.slider('Select months', 1, 36, step=3)
    try:
        data = get_stock_data(comp_info, days = num_month*30)
        st.markdown("**Stock data ({} months) : {} ({})**".format(num_month, comp_info['Name'], comp_info['Symbol']))
        filename = 'stockprice_{}_{}_{}m'.format(comp_info['Symbol'], comp_info['Name'], num_month)
        st.dataframe(data)
        download_df(data, filename)
    except ValueError:
        st.warning("Company '{}' information currently not avaliable".format(comp_info['Symbol']))

if __name__ == "__main__":
    main()
