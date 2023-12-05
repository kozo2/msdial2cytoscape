# msdial2cytoscape

## Getting Started
1. Download Docker Desktop fow Windows from https://www.docker.com/products/docker-desktop
2. Install and **Start** Docker Desktop
3. Open http://github.com/kozo2/msdial2cytoscape/zipball/main/ with your browser. (Your browser should then start downloading a zip file.)
4. Unzip the downloaded zip file.
5. Open the `dockercompose` foler and double-click the `run.bat` file.
6. Open http://localhost:6080/vnc_auto.html in your browser. You should see a Cytoscape window.
7. Open http://localhost:8501/ in your browser. You should see a Streamlit app named "msdial2cytoscape".
8. Upload your Cytoscape cys file (e.g. "my_pathway.cys") from the `1.Opening cytoscape session` link on the left in http://localhost:8501/ tab. (Then you should see your network in http://localhost:6080/vnc_auto.html tab.)
9. Upload your MS-DIAL alignment result table file (e.g. "my_msdial_result.txt") from the `2.Profile diagram mapping` link on the left in http://localhost:8501/ tab. (Then you should see your MS-DIAL profile in http://localhost:6080/vnc_auto.html tab.)
10. Switch Bar / Box plot from the `3.Switching bar or box` link on the left in http://localhost:8501/ tab.
11. Click `4. Download cys file` link and `Download cys` button on the left in in http://localhost:8501/ tab to download the Cytoscape network session to your local PC.

## Updating msdial2cytoscape

1. Run following command in Terminal
    ```
    docker-compose stop
    docker pull kozo2/msdial2cytoscape:latest
    docker-compose up -d
    ```
