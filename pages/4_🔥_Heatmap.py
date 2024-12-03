import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Heatmap")

with st.expander("See source code"):
    with st.echo():
        filepath = "https://github.com/lztzm/Geofile/blob/main/%E5%9C%96%E6%AA%94/%E8%87%BA%E4%B8%AD%E5%B8%82%E8%B7%AF%E5%A4%96%E5%81%9C%E8%BB%8A%E5%A0%B4%E5%BA%A7%E6%A8%99%E8%B3%87%E6%96%99.csv"
        m = leafmap.Map(center=[24.148805, 120.671363], zoom=4)
        m.add_heatmap(
            filepath,
            latitude="緯度(Y座標)",
            longitude="經度(X座標)",
            value="pop_max",
            name="Heat map",
            radius=20,
        )
m.to_streamlit(height=700)
