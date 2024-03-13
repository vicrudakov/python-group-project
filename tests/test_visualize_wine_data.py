import pytest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wine_data_analysis.visualize_wine_data import VisualizeWineData

@pytest.fixture
def example_data_set():
    # Create a temporary example data set 
    df_class = pd.DataFrame({'class': np.random.randint(low=1, high=4, size=10)})
    df_features = pd.DataFrame({f'Column_{i}': np.random.rand(10) for i in range(13)})
    df = df_class.reset_index(drop=True).join(df_features)
    return df 

def test_draw_histograms(example_data_set, capsys):
    # Initialize class VisualizeWineData with example dataset
    data_visualize = VisualizeWineData(data=example_data_set)
    
    # Call the data_visualize method
    _, axs = data_visualize.draw_histograms()
    
    # Perform asserts on data types
    assert all(isinstance(x, plt.Axes) for x in axs)
    
    # Perform assert on axis number
    assert len(axs) == len(example_data_set.columns) - 1

def test_draw_boxplots(example_data_set, capsys):
    # Initialize class VisualizeWineData with example dataset
    data_visualize = VisualizeWineData(data=example_data_set)
    
    # Call the data_visualize method
    _, axs = data_visualize.draw_boxplots()
    
    # Perform asserts on data types
    assert all(isinstance(x, plt.Axes) for x in axs)
    
    # Perform assert on axis number
    assert len(axs) == len(example_data_set.columns) - 1