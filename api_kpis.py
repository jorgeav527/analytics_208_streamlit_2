import streamlit as st


def kpi(title, icon, value):
    st.markdown(
        f"""
    <div class="kpi-card">
        <div class="kpi-title">{icon} {title}</div>
        <div class="kpi-value">{value:,}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

def plot_kpis(df):
    total_countries = len(df)
    total_population = df["population"].sum()
    avg_population = int(df["population"].mean())
    largest_area = df["area"].max()

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        kpi(title="Total Countries", icon="🌍", value=total_countries)

    with c2:
        kpi(title="Total Population", icon="👥", value=total_population)

    with c3:
        kpi(title="Avg Population", icon="📊", value=avg_population)

    with c4:
        kpi(title="Largest Area (km²)", icon="🌐", value=largest_area)