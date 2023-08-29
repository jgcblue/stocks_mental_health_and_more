import pandas as pd

def calculate_average_by_year(df, column_name):
    """
    Calculates the average value of a specified column by year.
    
    Parameters:
        df (DataFrame): Input DataFrame containing the data.
        column_name (str): Name of the column for which the average is calculated.
    
    Returns:
        DataFrame: A new DataFrame with 'Year' and 'Average' columns.
    """
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    average_per_year = df.groupby('Year')[column_name].mean()
    
    result_df = pd.DataFrame({'Year': average_per_year.index, 'Average': average_per_year.values})
    return result_df

def calculate_average_by_year_micro(df, column_name):
    """
    Calculates the average value of a specified column by year for a DataFrame with 'date' column.
    
    Parameters:
        df (DataFrame): Input DataFrame containing the data.
        column_name (str): Name of the column for which the average is calculated.
    
    Returns:
        DataFrame: A new DataFrame with 'year' and 'Average' columns.
    """
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    average_per_year = df.groupby('year')[column_name].mean()
    
    result_df = pd.DataFrame({'year': average_per_year.index, 'Average': average_per_year.values})
    return result_df

def read_stock_data(file_path):
    """
    Reads stock data from a CSV file and returns a DataFrame.
    
    Parameters:
        file_path (str): Path to the CSV file containing the stock data.
    
    Returns:
        DataFrame: The DataFrame containing the stock data.
    """
    return pd.read_csv(file_path)

def calculate_and_set_average_by_year(data_frame, date_column, price_column):
    """
    Calculates average closing prices by year and sets 'Year' as the index.
    
    Parameters:
        data_frame (DataFrame): Input DataFrame containing stock data.
        date_column (str): Name of the column with date information.
        price_column (str): Name of the column with price information.
    
    Returns:
        DataFrame: A new DataFrame with 'Year' as the index and calculated average closing prices.
    """
    average_data = data_frame.copy()
    average_data = calculate_average_by_year(average_data[[date_column, price_column]], price_column)
    average_data['Year'] = pd.to_datetime(average_data['Year'], format='%Y')
    average_data.set_index('Year', inplace=True)
    return average_data

def merge_and_drop_na(data_frames):
    """
    Merges DataFrames and drops rows with NaN values.
    
    Parameters:
        data_frames (list): List of DataFrames to be merged.
    
    Returns:
        DataFrame: The merged DataFrame with NaN rows dropped.
    """
    merged_data = pd.concat(data_frames, axis=1)
    merged_data_dropped = merged_data.dropna()
    return merged_data_dropped

def rename_columns(data_frame, column_names):
    """
    Renames columns of a DataFrame.
    
    Parameters:
        data_frame (DataFrame): Input DataFrame to be modified.
        column_names (list): List of new column names.
    
    Returns:
        DataFrame: The modified DataFrame with renamed columns.
    """
    data_frame.columns = column_names
    return data_frame

