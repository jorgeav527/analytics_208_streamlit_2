import pandas as pd
import requests
import streamlit as st

@st.cache_data
def get_data_api(url: str):
    response = requests.get(url)
    data = response.json()

    df = pd.json_normalize(data)
    df = df[["name.common", "region", "population", "area", "capital", "cca3"]].rename(
        columns={"name.common": "country"}
    )
    return df