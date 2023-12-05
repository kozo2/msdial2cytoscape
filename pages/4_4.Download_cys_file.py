import streamlit as st
import py4cytoscape as p4c
from datetime import datetime

def get_cys_file():
    current_datetime = datetime.now()
    p4c.save_session(filename = str(current_datetime).split(" ")[0], base_url='http://cytoscape-desktop:1234/v1')
    p4c.sandbox_get_from(str(current_datetime).split(" ")[0] + ".cys", base_url='http://cytoscape-desktop:1234/v1')

cysfile = get_cys_file()

if st.session_state['is_mapped']:
    with open(str(current_datetime).split(" ")[0] + ".cys", "rb") as file:
        btn = st.download_button(
            label="Download cys file",
            data=file,
            file_name="network.cys",
            mime="application/zip"
        )
