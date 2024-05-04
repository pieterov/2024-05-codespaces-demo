# Dit heb ik toegevoegd in branch update-cbs-data.
import pandas as pd
import cbsodata

c_search = "Ziekteverzuim"

# Downloading table list
df_toc = pd.DataFrame(cbsodata.get_table_list())

df_toc_ziekteverzuim = df_toc[
    df_toc['Title'].str.contains(c_search, na=False)
    ]