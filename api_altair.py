import streamlit as st
import altair as alt


def plot_altair_insights(df_filtered, region_name):
    df_plot = df_filtered.copy()
    df_plot["density"] = df_plot["population"] / df_plot["area"].replace(0, 1)

    chart = (
        alt.Chart(df_plot)
        .mark_circle(opacity=0.7, stroke="white", strokeWidth=1)
        .encode(
            x=alt.X(
                "population:Q", title="Total Population", axis=alt.Axis(format="~s")
            ),  # Readable numbers like 1M, 10M
            y=alt.Y(
                "density:Q",
                title="Population Density (People per km²)",
                scale=alt.Scale(zero=False),
            ),
            size=alt.Size(
                "area:Q", title="Land Area", scale=alt.Scale(range=[100, 3000])
            ),
            color=alt.Color(
                "density:Q", scale=alt.Scale(scheme="magma"), title="Density Intensity"
            ),
            tooltip=[
                alt.Tooltip("country", title="Country"),
                alt.Tooltip("population", title="Population", format=","),
                alt.Tooltip("area", title="Area (km²)", format=","),
                alt.Tooltip("density", title="Density (per km²)", format=".2f"),
            ],
        )
        .properties(
            width="container",
            height=500,
            title=f"Insight: Population vs. Density in {region_name} (Linear Scale)",
        )
        .interactive()
    )

    st.altair_chart(chart, width="stretch")


def plot_altair_benchmark(df_filtered, region_name):
    # 1. Sort the data for a clean descending look
    df_plot = df_filtered.sort_values("population", ascending=False)

    # 2. Create the main Bars
    bars = (
        alt.Chart(df_plot)
        .mark_bar(cornerRadiusTopRight=5, cornerRadiusBottomRight=5)
        .encode(
            x=alt.X("population:Q", title="Population", axis=alt.Axis(format="~s")),
            y=alt.Y("country:N", sort="-x", title="Country"),
            color=alt.Color(
                "population:Q", scale=alt.Scale(scheme="purples"), legend=None
            ),
            tooltip=["country", "population", "area"],
        )
    )

    # 5. Layer them together (+)
    chart = (
        (bars)
        .properties(
            width="container",
            height=500,  # Dynamic height based on number of countries
            title=f"Population Benchmark: {region_name}",
        )
        .configure_axis(labelFontSize=12, titleFontSize=14)
    )

    st.altair_chart(chart, width="stretch")