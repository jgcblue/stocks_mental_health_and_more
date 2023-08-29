import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

def perform_seasonal_decomposition(data_frame, model='additive'):
    """
    Perform seasonal decomposition for each column in the DataFrame.
    
    Parameters:
        data_frame (DataFrame): The input DataFrame containing time series data.
        model (str): The seasonal decomposition model to use: 'additive' or 'multiplicative'.
    
    Returns:
        dict: A dictionary containing decomposition results for each column.
    """
    decomposition_results = {}

    for col in data_frame.columns:
        result = seasonal_decompose(data_frame[col], model=model)
        decomposition_results[col] = {
            'trend': result.trend,
            'seasonal': result.seasonal,
            'resid': result.resid,
            'observed': result.observed
        }
    
    return decomposition_results

def plot_decomposition_components(components_dict):
    """
    Plot the decomposition components from the dictionary.
    
    Parameters:
        components_dict (dict): A dictionary containing decomposition results.
    """
    for col, components in components_dict.items():
        plt.figure(figsize=(10, 6))
        plt.suptitle(f'Seasonal Decomposition - {col}')
        
        plt.subplot(411)
        plt.plot(components['observed'], label='Original')
        plt.legend()
        
        plt.subplot(412)
        plt.plot(components['trend'], label='Trend')
        plt.legend()
        
        plt.subplot(413)
        plt.plot(components['seasonal'], label='Seasonal')
        plt.legend()
        
        plt.subplot(414)
        plt.plot(components['resid'], label='Residual')
        plt.legend()
        
        plt.tight_layout()
        plt.show()

# Assuming your DataFrame is named 'final'
# Make sure 'final' has the same structure as your provided data

# Get user input for the decomposition model
model_choice = input("Choose decomposition model ('additive' or 'multiplicative'): ").lower()
while model_choice not in ['additive', 'multiplicative']:
    print("Invalid choice. Please choose 'additive' or 'multiplicative'.")
    model_choice = input("Choose decomposition model ('additive' or 'multiplicative'): ").lower()

# Perform seasonal decomposition and store the results
decomposition_results = perform_seasonal_decomposition(final, model=model_choice)

# Plot the decomposition components
plot_decomposition_components(decomposition_results)

# Access the components like this:
print(decomposition_results['apple_closing_avg']['trend'])
print(decomposition_results['msft_closing_avg']['seasonal'])

