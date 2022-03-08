
def get_range_reading(values: list) -> str:
    values.sort()
    return f'{values[0]}-{values[-1]}, {len(values)}'
