import pandas as pd


def group_rare_categories(df, column, threshold):
    """
    Group rare categories in a categorical column into a new category 'Other'.

    Parameters:
    df (pd.DataFrame): DataFrame containing the categorical column.
    column (str): Name of the column to process.
    threshold (int): Minimum number of occurrences required for a category to remain unchanged.

    Returns:
    pd.DataFrame: DataFrame with rare categories grouped as 'Other'.
    """
    counts = df[column].value_counts()
    mask = counts[counts >= threshold].index
    df[column] = df[column].where(df[column].isin(mask), "Other")

    return df


def one_hot_encode(df, column):
    """
    Perform one-hot encoding on a categorical column.

    Parameters:
    df (pd.DataFrame): DataFrame containing the categorical column.
    column (str): Name of the column to encode.

    Returns:
    pd.DataFrame: DataFrame with one-hot encoded columns.
    """

    df = pd.get_dummies(df)
    return df


# Example data
data = {'color': ['red', 'blue', 'green', 'blue', 'red', 'yellow', 'green']}
df = pd.DataFrame(data)

# Apply the functions to the dataset
df = group_rare_categories(df, 'color', 2)
df_encoded = one_hot_encode(df, 'color')
print(df_encoded)
