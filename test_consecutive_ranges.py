import a2d_mapper
import consecutive_ranges


def test_get_range_reading_double_values():
    input_list = [[4, 5], [7, 8], [9, 10], [1, 5]]
    expected_output = [{(4, 5): 2}, {(7, 8): 2}, {(9, 10): 2}, {}]
    for indx, lists in enumerate(input_list):
        returned_value = consecutive_ranges.get_consecutive_numbers_count(lists)
        assert expected_output[indx] == returned_value


def test_get_range_reading_single_values():
    input_list = [[4], [0], [3]]
    expected_output = [{}, {}, {}]
    for indx, lists in enumerate(input_list):
        returned_value = consecutive_ranges.get_consecutive_numbers_count(lists)
        assert expected_output[indx] == returned_value


def test_get_range_reading_multiple_values():
    input_list = [[4, 5, 5, 7, 7, 7, 8], [1, 3, 3, 4, 5, 8, 9, 10], [3, 3, 5, 4, 10, 11, 12]]
    expected_output = [{(4, 5): 3, (7, 8): 4}, {(3, 5): 4, (8, 10): 3}, {(3, 5): 4, (10, 12): 3}]
    for indx, lists in enumerate(input_list):
        returned_value = consecutive_ranges.get_consecutive_numbers_count(lists)
        assert expected_output[indx] == returned_value


def test_invalid_ranges():
    assert a2d_mapper.map_adc_values_to_range([], a2d_mapper.A2D_12Bit) == {}
    assert a2d_mapper.map_adc_values_to_range([0], a2d_mapper.A2D_12Bit) == {}
    assert a2d_mapper.map_adc_values_to_range([], a2d_mapper.A2D_10Bit) == {}
    assert a2d_mapper.map_adc_values_to_range([0], a2d_mapper.A2D_10Bit) == {}


def test_valid_ranges():
    assert a2d_mapper.map_adc_values_to_range([2223, 2214, 1190, 658, 2103, 9, 2588],
                                              a2d_mapper.A2D_12Bit) == {(2, 3): 2, (5, 6): 4}
    assert a2d_mapper.map_adc_values_to_range([48, 21, 327, 839, 184, 51, 642],
                                              a2d_mapper.A2D_12Bit) == {(0, 2): 7}

    assert a2d_mapper.map_adc_values_to_range([3000, 400, 500, 600, 650, 700, 750, 800],
                                              a2d_mapper.A2D_10Bit) == {(3, 4): 2, (6, 8): 3}
    assert a2d_mapper.map_adc_values_to_range([3000, 400, 500, 600, 650],
                                              a2d_mapper.A2D_10Bit) == {(3, 4): 2}


if __name__ == "__main__":
    test_get_range_reading_single_values()
    test_get_range_reading_double_values()
    test_get_range_reading_multiple_values()
    test_invalid_ranges()
    test_valid_ranges()
