import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Marker Cluster")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[24.14734503954353, 120.67316364818225], zoom=10)
        filepath = pd.read_csv("https://raw.githubusercontent.com/lztzm/Geofile/main/%E5%9C%96%E6%AA%94/%E8%87%BA%E4%B8%AD%E5%B8%82%E8%B7%AF%E5%A4%96%E5%81%9C%E8%BB%8A%E5%A0%B4%E5%BA%A7%E6%A8%99%E8%B3%87%E6%96%99.csv")

        m.add_points_from_xy(
            filepath,
            x="緯度(Y座標)",
            y="經度(X座標)",
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=700)
