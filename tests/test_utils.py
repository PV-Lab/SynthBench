import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from synthbench.utils import save, icsd_finder
import pandas as pd
import pytest
import os

def test_addition():
    assert 1 + 1 == 2
    assert 2 + 2 == 4

def test_mult():
    assert 2 * 2 == 4

def test_save():
    filter_name = "func_save"
    df = pd.read_csv("./test_files/df_dummy.csv")
    df_name = "test_save"
    filename = save(filter_name, df, df_name)

    # Check if the file is created
    assert os.path.exists(filename)

    # Check if the saved file is same as the original DataFrame
    saved_df = pd.read_csv(filename)
    pd.testing.assert_frame_equal(df, saved_df)
    
    

def test_icsd_finder():
    icsd_true = pd.read_csv("./test_files/icsd_dummy.csv")
    nov_mat = pd.read_csv("./test_files/df_dummy.csv")
    nov_mat, tp_count = icsd_finder(icsd_true, nov_mat)

    # Check if the 'icsd_ids' column is added to nov_mat
    assert 'icsd_ids' in nov_mat.columns

    


