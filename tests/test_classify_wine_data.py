import pytest
import pandas as pd
import numpy as np
from wine_data_analysis.classify_wine_data import ClassifyWineData

@pytest.mark.parametrize("y, expected_accuracy", [
    ([1, 2, 3, 2, 3, 1, 2, 1, 3], 0.4), # y_test: [1, 2, 1, 1, 3]
    ([2, 3, 1, 1, 2, 2, 3, 1, 1], 0.6), # y_test: [3, 3, 2, 2, 1]
    ([2, 3, 2, 2, 2, 1, 1, 2, 2], 0.2) # y_test: [2, 3, 1, 2, 2]
])
def test_accuracy(y, expected_accuracy):
    y_pred = [1, 2, 3, 2, 1]
    df = pd.DataFrame({'class': y})
    data_classify = ClassifyWineData(df, test_size = 5)
    assert data_classify.accuracy(y_pred) == expected_accuracy


@pytest.mark.parametrize("y, expected_average_precision", [
    ([1, 2, 3, 2, 3, 1, 2, 1, 3], 0.33333333), # y_test: [1, 2, 1, 1, 3]
    ([2, 3, 1, 1, 2, 2, 3, 1, 1], 0.5), # y_test: [3, 3, 2, 2, 1]
    ([2, 3, 2, 2, 2, 1, 1, 2, 2], 0.166666666) # y_test: [2, 3, 1, 2, 2]
])
def test_average_precision(y, expected_average_precision):
    y_pred = np.array([1, 2, 3, 2, 1])
    df = pd.DataFrame({'class': y})
    data_classify = ClassifyWineData(df, test_size = 5)
    assert np.isclose(data_classify.average_precision(y_pred), expected_average_precision, atol=1e-4) 

@pytest.mark.parametrize("y, expected_average_recall", [
    ([1, 2, 3, 2, 3, 1, 2, 1, 3], 0.44444444), # y_test: [1, 2, 1, 1, 3]
    ([2, 3, 1, 1, 2, 2, 3, 1, 1], 0.5), # y_test: [3, 3, 2, 2, 1]
    ([2, 3, 2, 2, 2, 1, 1, 2, 2], 0.11111111) # y_test: [2, 3, 1, 2, 2]
])
def test_average_recall(y, expected_average_recall):
    y_pred = np.array([1, 2, 3, 2, 1])
    df = pd.DataFrame({'class': y})
    data_classify = ClassifyWineData(df, test_size = 5)
    assert np.isclose(data_classify.average_recall(y_pred), expected_average_recall, atol=1e-4)