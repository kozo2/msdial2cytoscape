import streamlit as st
import py4cytoscape as p4c
import re

if st.session_state['is_mapped']:
    viz_bar_inchi1st = st.button("Visualize bar chart [The InChIKey mapping is performed using only the first block of the string]")
    viz_bar_inchi2nd = st.button("Visualize bar chart [The InChIKey mapping is performed using the first and second blocks of the string]")
    viz_bar_inchi3rd = st.button("Visualize bar chart [The InChIKey mapping is performed using the first, second, and third blocks of the string]")

    viz_box_inchi1st = st.button("Visualize box chart [The InChIKey mapping is performed using only the first block of the string]")
    viz_box_inchi2nd = st.button("Visualize box chart [The InChIKey mapping is performed using the first and second blocks of the string]")
    viz_box_inchi3rd = st.button("Visualize box chart [The InChIKey mapping is performed using the first, second, and third blocks of the string]")
    
    if viz_bar_inchi3rd:
        current_style = p4c.get_current_style(base_url='http://cytoscape-desktop:1234/v1')
        mvp = p4c.map_visual_property("NODE_CUSTOMGRAPHICS_1", "barimgpath", "p", base_url='http://cytoscape-desktop:1234/v1')
        p4c.update_style_mapping(current_style, mvp, base_url='http://cytoscape-desktop:1234/v1')
        st.success('Done! Please check if bar chart is mapped in http://localhost:6080/vnc_auto.html')
    
    if viz_box_inchi3rd:
        current_style = p4c.get_current_style(base_url='http://cytoscape-desktop:1234/v1')
        mvp = p4c.map_visual_property("NODE_CUSTOMGRAPHICS_1", "boximgpath", "p", base_url='http://cytoscape-desktop:1234/v1')
        p4c.update_style_mapping(current_style, mvp, base_url='http://cytoscape-desktop:1234/v1')
        st.success('Done! Please check if box plot is mapped in http://localhost:6080/vnc_auto.html')
    
    if viz_bar_inchi1st:
        st.write("Button clicked, but it does nothing!")
    
    if viz_bar_inchi2nd:
        st.write("Button clicked, but it does nothing!")

    if viz_box_inchi1st:
        st.write("Button clicked, but it does nothing!")
    
    if viz_box_inchi2nd:
        st.write("Button clicked, but it does nothing!")