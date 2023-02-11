import pandas as pd
import numpy as np

def create_and_save_dataframe():
    df = pd.DataFrame(np.random.randn(100, 500), columns=[f"col_{i}" for i in range(500)])
    df.to_parquet("scripts/app/files/data/dummy_df.parq", index=False)

create_and_save_dataframe()