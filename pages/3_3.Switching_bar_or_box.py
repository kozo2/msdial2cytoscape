import streamlit as st
import py4cytoscape as p4c
import re

if st.session_state['is_mapped']:
    viz_bar = st.button("Visualize bar chart")
    viz_box = st.button("Visualize box chart")
    if viz_bar:
        current_style = p4c.get_current_style(base_url='http://cytoscape-desktop:1234/v1')
        mvp = p4c.map_visual_property("NODE_CUSTOMGRAPHICS_1", "barimgpath", "p", base_url='http://cytoscape-desktop:1234/v1')
        p4c.update_style_mapping(current_style, mvp, base_url='http://cytoscape-desktop:1234/v1')
        st.success('Done! Please check if bar chart is mapped in http://localhost:6080/vnc_auto.html')
    
    if viz_box:
        current_style = p4c.get_current_style(base_url='http://cytoscape-desktop:1234/v1')
        mvp = p4c.map_visual_property("NODE_CUSTOMGRAPHICS_1", "boximgpath", "p", base_url='http://cytoscape-desktop:1234/v1')
        p4c.update_style_mapping(current_style, mvp, base_url='http://cytoscape-desktop:1234/v1')
        st.success('Done! Please check if box plot is mapped in http://localhost:6080/vnc_auto.html')
        