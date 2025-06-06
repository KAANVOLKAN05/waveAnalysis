import pytest
import numpy as np
from waveanalysis.image_props.image_bin_calc import create_kymo_bin_array

import json

@pytest.fixture
def default_bin_values():
    return [
        np.load('tests/assets/kymo/numpy_arrays/kymo_1_Group1.tif_bin_values.npy'),
        np.load('tests/assets/kymo/numpy_arrays/kymo_1_Group2.tif_bin_values.npy')
    ]
     
def test_kymo_bin_calc(default_bin_values):
    default_arrays = [
        np.load('tests/assets/kymo/numpy_arrays/kymo_1_Group1_array.npy'),
        np.load('tests/assets/kymo/numpy_arrays/kymo_1_Group2_array.npy')
    ]

    default_dicts = [
        'tests/assets/kymo/dicts_lists/kymo_image_properties_1_Group1_final.json',
        'tests/assets/kymo/dicts_lists/kymo_image_properties_1_Group2_final.json'
    ]

    for array, known_results, img_props_file in zip(default_arrays, default_bin_values, default_dicts):
        with open(img_props_file, 'r') as file:
            img_props_dict = json.load(file)
        exp_results, _ = create_kymo_bin_array(array, img_props_dict)

        assert np.array_equal(known_results, exp_results)