import streamlit as st
import py4cytoscape as p4c
import re

if st.session_state['is_mapped']:

    st.header("3. Switching the visualization type")

    st.subheader("Visualize BAR chart")
    viz_bar_inchi1st = st.button("Visualize BAR chart [The InChIKey mapping using **only the 1st block**]")
    viz_bar_inchi2nd = st.button("Visualize BAR chart [The InChIKey mapping using **the 1st and 2nd blocks**]")
    viz_bar_inchi3rd = st.button("Visualize BAR chart [The InChIKey mapping using **all its blocks**]")

    st.subheader("Visualize BOX chart")
    viz_box_inchi1st = st.button("Visualize BOX chart [The InChIKey mapping using **only the 1st block**]")
    viz_box_inchi2nd = st.button("Visualize BOX chart [The InChIKey mapping using **the 1st and 2nd blocks**]")
    viz_box_inchi3rd = st.button("Visualize BOX chart [The InChIKey mapping using **all its blocks**]")
    
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