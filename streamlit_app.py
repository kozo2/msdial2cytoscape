import streamlit as st
import pandas as pd
import anndata as ad
import scanpy as sc
import seaborn as sns
import py4cytoscape as p4c

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

# Upload TSV file
uploaded_file = st.file_uploader("Upload a TSV file", type="txt")

if cys_file is not None:
    p4c.sandbox_send_to(cys_file, base_url='http://cytoscape-desktop:1234/v1')
    p4c.open_session(cys_file, base_url='http://cytoscape-desktop:1234/v1')

# Once a file is uploaded
if uploaded_file is not None:
    # Read the file into a Pandas DataFrame
    data = pd.read_csv(uploaded_file, sep='\t', header=None)
    adata = to_anndata(data)

    # Button to perform hierarchical clustering
    if st.button('Cluster Data and Show Heatmap'):
        # # Perform hierarchical clustering
        # linkage = sch.linkage(data, method='ward')
        # dendrogram = sch.dendrogram(linkage)
        # cluster_ids = sch.fcluster(linkage, t=1.5, criterion='distance')

        # # Create a heatmap
        # fig = sns.clustermap(data, method='ward', cmap='viridis', standard_scale=1)
        fig = sc.pl.clustermap(adata)
        st.pyplot(fig)
else:
    st.write("Upload a TSV file to get started.")
