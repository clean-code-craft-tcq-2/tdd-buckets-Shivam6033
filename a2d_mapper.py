from consecutive_ranges import *

A2D_12Bit = {"max_allowed_value": 4094, "origin": 0, "max_current_value": 10}
A2D_10Bit = {"max_allowed_value": 511, "origin": 511, "max_current_value": 15}


def map_adc_values_to_range(A2Dvalues, A2D_map):
    result = []
    for value in A2Dvalues:
        value = value - ADC_dict["origin"]
        if value <= ADC_dict["max_allowed_value"]:
            result.append(round((value / ADC_dict["max_allowed_value"]) * ADC_dict["max_current_value"]))
    consecutive_count_map = get_consecutive_numbers_count(result)
    return consecutive_count_map



