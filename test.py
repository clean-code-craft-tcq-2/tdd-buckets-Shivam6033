import main


def test_get_range_reading():
    input_list = [4, 5]
    expected_output = "4-5, 2"
    returned_value = main.get_range_reading(input_list)
    assert expected_output == returned_value


if __name__ == "__main__":
    test_get_range_reading()
