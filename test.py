import main


def test_get_range_reading_double_values():
    input_list = [[4, 5], [7, 8], [9, 10], [1, 5]]
    expected_output = ["4-5 : 2\n", "7-8 : 2\n", "9-10 : 2\n", ""]
    for indx, lists in enumerate(input_list):
        returned_value = main.get_range_reading(lists)
        assert expected_output[indx] == returned_value


def test_get_range_reading_single_values():
    input_list = [[4], [0], [3]]
    expected_output = ""
    for lists in input_list:
        returned_value = main.get_range_reading(lists)
        assert expected_output == returned_value


def test_get_range_reading_multiple_values():
    input_list = [[4, 5, 5, 7, 7, 7, 8], [1, 3, 3, 4, 5, 8, 9, 10], [3, 3, 5, 4, 10, 11, 12]]
    expected_output = ["4-5 : 3\n7-8 : 4\n", "3-5 : 4\n8-10 : 3\n", "3-5 : 4\n10-12 : 3\n"]
    for indx, lists in enumerate(input_list):
        returned_value = main.get_range_reading(lists)
        assert expected_output[indx] == returned_value


if __name__ == "__main__":
    test_get_range_reading_single_values()
    test_get_range_reading_double_values()
    test_get_range_reading_multiple_values()
