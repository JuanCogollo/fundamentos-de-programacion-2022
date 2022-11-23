def flatten(list_):
    return [item for sublist in list_ for item in sublist]


def flatten_2(list_):
    flat_list = []
    for sublist in list_:
        for item in sublist:
            flat_list.append(item)

    return flat_list
