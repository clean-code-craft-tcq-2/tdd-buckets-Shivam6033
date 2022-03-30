import more_itertools


def get_range(lst):
    return [list(group) for group in more_itertools.consecutive_groups(lst)]


def get_reading_count(item, lst):
    count = 0
    for i in range(item[0], item[-1] + 1):
        count = count + lst.count(i)
    return count


def get_consecutive_numbers_count(lis):
    range_dict = {}
    lis.sort()
    ranges = get_range(lis)
    for item in ranges:
        if len(item) != 1:
            range_dict.update({(item[0], item[-1]): get_reading_count(item, lis)})
    return range_dict



