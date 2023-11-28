# msdial2cytoscape

## Getting Started
1. Download Docker Desktop from https://www.docker.com/products/docker-desktop
2. Install and Start Docker Desktop
3. Run following command in Terminal
    ```
    mkdir m2c
    cd m2c
    curl -O https://raw.githubusercontent.com/kozo2/msdial2cytoscape/main/dockercompose/.env
    curl -O https://raw.githubusercontent.com/kozo2/msdial2cytoscape/main/dockercompose/compose.yml
    docker-compose up -d
    ```
4. Open http://localhost:6080/vnc_auto.html in your browser. You should see a Cytoscape window.
5. Open http://localhost:8501/ in your browser. You should see a Streamlit app named "msdial2cytoscape".
6. Upload your Cytoscape cys file (e.g. "my_pathway.cys") from the `1.Opening cytoscape session` link on the left in http://localhost:8501/ tab. (Then you should see your network in http://localhost:6080/vnc_auto.html tab.)
7. Upload your MS-DIAL alignment result table file (e.g. "my_msdial_result.txt") from the `2.Profile diagram mapping` link on the left in http://localhost:8501/ tab. (Then you should see your MS-DIAL profile in http://localhost:6080/vnc_auto.html tab.)
8. Switch Bar / Box plot from the `3.Switching bar or box` link on the left in http://localhost:8501/ tab.
