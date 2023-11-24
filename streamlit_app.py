import streamlit as st
import pandas as pd
import anndata as ad
import seaborn as sns
import py4cytoscape as p4c
import re

def is_inchikey(string):
    """
    Check if a string is a valid InChIKey.
    
    Args:
    string (str): The string to check.

    Returns:
    bool: True if the string is a valid InChIKey, False otherwise.
    """
    pattern = r"^[A-Z]{14}-[A-Z]{10}-[A-Z\d]$"
    return bool(re.match(pattern, string))

def to_anndata(df: pd.DataFrame) -> ad.AnnData:
    df_row = df.iloc[:, 0:28]
    df_col = df.iloc[:, 28:]

    df_col_avgstd_removed = df_col.loc[:, ~df_col.iloc[3].str.contains('Average|Stdev')]
    counts = df_col_avgstd_removed.iloc[5:]
    counts_converted = counts.applymap(lambda x: pd.to_numeric(x, errors='coerce'))

    adata = ad.AnnData(counts_converted)
    adata.obs_names = [f"AlignmentID_{i:d}" for i in range(adata.n_obs)]
    adata.var_names = df_col_avgstd_removed.iloc[4]

    # prompt: remove the first 4 rows from df_row
    df_row = df_row.iloc[4:]

    # prompt: set the first row as column names of df_row
    df_row.columns = df_row.iloc[0]
    # prompt: remove the first row from df_row
    df_row = df_row.drop(df_row.index[0])
    # prompt: remove RangeIndex from df_row
    df_row = df_row.reset_index(drop=True)
    # prompt: drop `Alignment ID` column from df_row
    df_row = df_row.drop('Alignment ID', axis=1)

    adata.obs = df_row
    adata.var["Class"] = list(df_col_avgstd_removed.iloc[0])
    adata.var["File type"] = list(df_col_avgstd_removed.iloc[1])
    adata.var["Injection order"] = list(df_col_avgstd_removed.iloc[2])
    adata.var["Batch ID"] = list(df_col_avgstd_removed.iloc[3])

    return adata

# Streamlit page configuration
st.set_page_config(page_title="msdial2cytoscape", layout="wide")

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

# Upload TSV file
uploaded_file = st.file_uploader("Upload a TSV file", type="txt")

# Once a file is uploaded
if uploaded_file is not None:
    # Read the file into a Pandas DataFrame
    data = pd.read_csv(uploaded_file, sep='\t', header=None)
    adata = to_anndata(data)

    nodetable = p4c.get_table_columns(base_url='http://cytoscape-desktop:1234/v1')

    nodetblindex = []
    barimgpath = []
    boximgpath = []
    for index, row in nodetable.iterrows():
        inchikey = row['XrefId']
        nodetblindex.append(index)
        barimgpath.append("")
        boximgpath.append("")
        if is_inchikey(inchikey):
            bdata = adata[adata.obs.INCHIKEY == inchikey]
            if len(bdata.X) > 0:
                tmp = bdata.var[['Class', 'File type']]
                tmp['X'] = list(bdata.X[0])

                barplt = sns.catplot(data=tmp, x="Class", y="X", kind="bar")
                barpngfilename = "bar_" + inchikey + ".png"
                barplt.savefig(barpngfilename)
                p4c.sandbox_send_to(barpngfilename, base_url='http://cytoscape-desktop:1234/v1')
                barimgpath.pop()
                barimgpath.append("file:/root/CytoscapeConfiguration/filetransfer/default_sandbox/" + barpngfilename)

                boxplt = sns.catplot(data=tmp, x="Class", y="X", kind="box")
                boxpngfilename = "box_" + inchikey + ".png"
                boxplt.savefig(boxpngfilename)
                p4c.sandbox_send_to("box_" + inchikey + ".png", base_url='http://cytoscape-desktop:1234/v1')
                boximgpath.pop()
                boximgpath.append("file:/root/CytoscapeConfiguration/filetransfer/default_sandbox/" + boxpngfilename)
    
    df4send = pd.DataFrame(data={'barimgpath': barimgpath, 'boximgpath': boximgpath})
    df4send.index = nodetblindex
    p4c.load_table_data(df4send, base_url='http://cytoscape-desktop:1234/v1', table_key_column='SUID')

#     # Button to perform hierarchical clustering
#     if st.button('Cluster Data and Show Heatmap'):
#         # # Perform hierarchical clustering
#         # linkage = sch.linkage(data, method='ward')
#         # dendrogram = sch.dendrogram(linkage)
#         # cluster_ids = sch.fcluster(linkage, t=1.5, criterion='distance')

#         # # Create a heatmap
#         # fig = sns.clustermap(data, method='ward', cmap='viridis', standard_scale=1)
#         fig = sc.pl.clustermap(adata)
#         st.pyplot(fig)
# else:
#     st.write("Upload a TSV file to get started.")
