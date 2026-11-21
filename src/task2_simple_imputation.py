import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame


def impute_missing_values(df):
    """
    Impute missing values in the dataset using mean, median, and mode.

    Parameters:
    df (pd.DataFrame): DataFrame with missing values.

    Returns:
    pd.DataFrame: DataFrame with missing values imputed.
    """
    n = df.shape[0]
    df["A"] = df["A"].fillna(df["A"].sum() / df["A"].count())
    df["B"] = df["B"].fillna(df["B"].sort_values()[n // 2])
    df["C"] = df["C"].fillna(df["C"].mode()[0])
    return df


# Example data
data = {
    'A': [1, 2, None, 4],
    'B': [5, None, 7, 8],
    'C': ['cat', None, 'dog', 'dog']
}
df = pd.DataFrame(data)

# Apply the function to the dataset
df_imputed = impute_missing_values(df)
print(df_imputed)