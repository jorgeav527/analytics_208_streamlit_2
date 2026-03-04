import streamlit as st

from data_loader import get_data_api
from api_kpis import plot_kpis
from api_altair import plot_altair_insights, plot_altair_benchmark

st.set_page_config(layout="wide", page_title="Dashboard Pro", page_icon="📊")

st.markdown("""
<style>
.kpi-card {
    background: #ffffff;
    padding: 10px;
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    display: flex;
    flex-direction: column;
    gap: 8px;
    width: 220px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    border: 1px solid #f0f0f0;
}

.kpi-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
}

.kpi-title {
    font-size: 14px;
    font-weight: 600;
    color: #4a5568;
    display: flex;
    align-items: center;
    gap: 6px;
}

.kpi-value {
    font-size: 26px;
    font-weight: 700;
    color: #1a202c;
}

.kpi-container {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🛠️ Configuración")
api_url_input = st.sidebar.text_input(
    "URL",
    value="https://restcountries.com/v3.1/all?fields=name,region,population,area,capital,cca3",
)

df_api = get_data_api(api_url_input)

region = st.sidebar.selectbox("Región", df_api["region"].unique())

df_api_filtered = df_api[df_api["region"] == region]

tab_api, tab_csv = st.tabs(["🌍 API Data Analysis", "📈 Gapminder CSV Analysis"])


with tab_api:
    top_left, top_right = st.columns((2, 1))
    with top_left:
        st.subheader("📊 Key Metrics")
        plot_kpis(df_api_filtered)

    st.divider()

    mid_left, mid_right = st.columns(2)
    with mid_left:
        st.subheader("📊 Análisis de Correlación: Población vs PIB")
        plot_altair_insights(df_filtered=df_api_filtered, region_name=region)
    with mid_right:
        st.subheader("📋 Análisis de Barras: Población vs País")
        plot_altair_benchmark(df_filtered=df_api_filtered, region_name=region)

st.divider()
st.dataframe(df_api_filtered)
