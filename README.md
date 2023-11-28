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
6. Upload your Cytoscape cys file (e.g. "my_pathway.cys") to the first button in http://localhost:8501/ .
7. Upload your MS-DIAL alignment result table file (e.g. "my_msdial_result.txt") to the second button in http://localhost:8501/ .
