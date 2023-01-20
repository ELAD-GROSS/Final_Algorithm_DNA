from Improvement.add_meta_data import *


def remove_meta_data(sections_num, strings_list, frequency, letters_amount, read_size, max_splits_arr):
    strings_list = remove_padding(sections_num, strings_list, read_size, letters_amount, max_splits_arr)
    return remove_classifications(sections_num, strings_list, frequency, letters_amount)


def remove_padding(sections_amount, strings_list, read_size, letters_amount, max_splits_arr):
    # TODO: find the bug
    for section_num in range(sections_amount):
        if section_num == 0:
            strings_list[section_num] = strings_list[section_num][: -read_size + max_splits_arr[section_num][1] + letters_amount]

        elif section_num == sections_amount - 1:
            strings_list[section_num] = strings_list[section_num][read_size - max_splits_arr[section_num][0]:]
        else:
            strings_list[section_num] = strings_list[section_num][read_size - max_splits_arr[section_num][0]: -read_size + max_splits_arr[section_num][1] + letters_amount]
    return strings_list


def remove_classifications(sections_amount, strings_list, frequency, letters_amount):
    # TODO: maybe there is a bug here as well?
    sections = []
    for section_num in range(sections_amount):
        sub_sections = textwrap.wrap(strings_list[section_num], width=frequency + letters_amount, break_long_words=True)
        section = "".join(sub_section[letters_amount:] for sub_section in sub_sections)
        sections.append(section[:-letters_amount])

    strand_rebuilt = "".join(sections)
    return strand_rebuilt


