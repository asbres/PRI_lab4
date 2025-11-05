import pytest
import pandas as pd
from main import get_gender_counts


@pytest.fixture
def sample_df():
    data = {
        "Pclass": [1, 3, 3, 1, 2, 2, 3],
        "Sex": ["male", "male", "female", "male", "female", "male", "female"]
    }
    return pd.DataFrame(data)


def test_get_gender_counts_class1(sample_df):
    men, women = get_gender_counts(sample_df, 1)
    assert men == 2
    assert women == 0


def test_get_gender_counts_class2(sample_df):
    men, women = get_gender_counts(sample_df, 2)
    assert men == 1
    assert women == 1


def test_get_gender_counts_class3(sample_df):
    men, women = get_gender_counts(sample_df, 3)
    assert men == 1
    assert women == 2


def test_get_gender_counts_empty(sample_df):
    men, women = get_gender_counts(sample_df, 99)
    assert men == 0
    assert women == 0
