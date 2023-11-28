import streamlit as st
import py4cytoscape as p4c

st.set_page_config(
    page_title="Open Cytoscape .cys file",
)

# Title of the app
st.title("msdial2cytoscape")

# Upload cys file
cys_file = st.file_uploader("Upload a Cytoscape session [cys] file", type="cys")

if cys_file is not None:
    with st.spinner('Loading Cytoscape session [cys] file...'):
        with open(cys_file.name, 'wb') as f:
            f.write(cys_file.getbuffer())
        p4c.sandbox_send_to(cys_file.name, base_url='http://cytoscape-desktop:1234/v1')
        p4c.open_session(cys_file.name, base_url='http://cytoscape-desktop:1234/v1')
    st.success('Done! Please check if your network is visible on http://localhost:6080/vnc_auto.html')
else:
    st.write("Upload a Cytoscape session [cys] to get started.")
