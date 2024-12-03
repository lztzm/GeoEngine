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
        filepath = "https://github.com/lztzm/Geofile/blob/main/圖檔/臺中市路外停車場座標資料.csv"
        m = leafmap.Map(center=[24.14734503954353, 120.67316364818225], zoom=)
        m.add_heatmap(
            filepath,
            latitude="緯度(Y座標)",
            longitude="經度(X座標)",
            value="位址",
            name="Heat map",
            radius=20,
        )
m.to_streamlit(height=700)
