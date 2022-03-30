from collections import Counter


def get_consecutive_sublist(lis):
    pointer = 0
    main_list = []
    sub_list = []
    while pointer < len(lis):
        if pointer == 0:
            sub_list.append(lis[pointer])
            pointer = pointer + 1
            continue
        else:
            if lis[pointer] == lis[pointer - 1]:
                pointer = pointer + 1
                continue
            elif lis[pointer] == lis[pointer - 1] + 1:
                sub_list.append(lis[pointer])
            elif lis[pointer] != lis[pointer - 1] + 1:
                main_list.append(sub_list)
                sub_list = []
                sub_list.append(lis[pointer])
        if pointer == len(lis) - 1:
            main_list.append(sub_list)
        pointer += 1
    return main_list


def get_items_count(iterable: list):
    return dict(Counter(iterable))


def get_ranges_count(sublist, items_count_mapper):
    string = ""
    for sub_list in sublist:
        summation = 0
        if len(sub_list) > 1:
            string = string + f"{sub_list[0]}-{sub_list[-1]}"
            for items in range(sub_list[0], sub_list[-1] + 1):
                summation = summation + items_count_mapper[items]
            string = string + f" : {summation}\n"
    return string


def get_range_reading(values: list) -> str:
    values.sort()
    sublist = get_consecutive_sublist(values)
    items_count_mapper = get_items_count(values)
    string = get_ranges_count(sublist, items_count_mapper)
    return string
