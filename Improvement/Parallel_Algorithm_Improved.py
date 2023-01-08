from multiprocessing import Process, Manager
from Original_Algorithm.algorithm import final_algorithm
from Improvement.Utilities import get_section_size, create_convert_list
from Improvement.declassify_reads_improvement import declassify_reads
from Improvement.find import find_longest


is_failed = -1


def run_section_algorithm(section_reads_lst: list, section_len, read_size,
                          real_edge_length,
                          complete_sections_dict, section):
    candidate_results = final_algorithm(section_len, read_size, real_edge_length, section_reads_lst)

    if candidate_results is None or len(candidate_results) != 1:
        complete_sections_dict[is_failed] = 1

    else:
        complete_sections_dict[section] = candidate_results[0]


def run_parallel_algorithm(reads_lst, read_size, real_edge_length,
                           special_sections_length):
    """
    :param paddings_by_sections: A list of sections, in each item has a list of padding position
           (weather starting at beginning of read, end of read or has no padding)
    :param reads_lst: Each item of the list is a list of reads that is classified by a section
    :param read_size: The size of a read
    :param real_edge_length: A parameter for the original algorithm
    :param special_sections_length: The length of the first/last sections including classifications.
           In order to get the other sections' lengths, add read_size - letters_amount to this
    :param letters_amount: Amount of letters used for classifying the string to sections
    :return: If successful, then a list containing the sections of the original string, otherwise the list will have
             Nones in it which will indicate that the algorithm failed in at least one of the parallel sections
    """
    processes = []
    section_amount = len(reads_lst)
    manager = Manager()
    shared_dict = manager.dict()
    complete_sections = []

    for section in range(section_amount):
        if 0 < section < section_amount - 1:
            section_len = special_sections_length + read_size

        else:
            section_len = special_sections_length

        p = Process(target=run_section_algorithm,
                    args=(
                        reads_lst[section], int(section_len), read_size,
                        real_edge_length, shared_dict, section))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    if is_failed in shared_dict.keys():
        return None

    for section_num in range(section_amount):
        complete_sections.append(shared_dict[section_num])
    return complete_sections



def run_parallel_algorithm_not_really_parallel(reads_lst, read_size, real_edge_length,
                           special_sections_length):
    """
    :param paddings_by_sections: A list of sections, in each item has a list of padding position
           (weather starting at beginning of read, end of read or has no padding)
    :param reads_lst: Each item of the list is a list of reads that is classified by a section
    :param read_size: The size of a read
    :param real_edge_length: A parameter for the original algorithm
    :param special_sections_length: The length of the first/last sections including classifications.
           In order to get the other sections' lengths, add read_size - letters_amount to this
    :param letters_amount: Amount of letters used for classifying the string to sections
    :return: If successful, then a list containing the sections of the original string, otherwise the list will have
             Nones in it which will indicate that the algorithm failed in at least one of the parallel sections
    """

    section_amount = len(reads_lst)
    shared_dict = dict()
    complete_sections = []

    for section in range(section_amount):
        if 0 < section < section_amount - 1:
            section_len = special_sections_length + read_size

        else:
            section_len = special_sections_length

        run_section_algorithm(reads_lst[section], int(section_len), read_size,
                        real_edge_length, shared_dict, section)


    if is_failed in shared_dict.keys():
        return None

    for section_num in range(section_amount):
        complete_sections.append(shared_dict[section_num])
    return complete_sections


# def final_algorithm(sections_num, letters_amount, real_edge_len, frequency, strand_len, padding_size, read_size,
#                     read_lst):
#     # declassify each read by its section
#     four_pow = create_convert_list(read_size)
#     try:
#         # TODO: create these two functions
#         classifications = create_longest_classifications(letters_amount, sections_num)
#         paddings_hash = create_padddins_hash()
#         paddings_to_classifications = {}
#
#         for i in range(sections_num - 1):
#             padding_letters = classifications[i][0] + classifications[i + 1]
#             paddings_to_classifications[padding_letters] = [classifications[i], classifications[i + 1]]
#
#     except ValueError:
#         print("Can't create this many sections with only this amount of letters")
#         exit(0)
#
#     reads_by_sections, paddings_by_sections = declassify_reads(read_lst, frequency, letters_amount, classifications,
#                                                                padding_size, paddings_hash, four_pow,
#                                                                paddings_to_classifications, sections_num)
#
#     # def declassify_reads(reads, freq, letters_amount, classifications, padding_size, paddings_hash, four_pow,
#     #                      pad_to_candidates, num_of_sections):
#
#     # run for each section Alex's algorithm
#     # TODO: finish going over this algorithm, the parallel algorithm functions and remove meta data functions
#     strand_section_len_before = strand_len / sections_num
#     special_section_length = get_section_size(strand_section_len_before, frequency, read_size, letters_amount)
#     complete_sections = run_parallel_algorithm(reads_by_sections, paddings_by_sections, read_size,
#                                                real_edge_len, special_section_length,
#                                                letters_amount)
#
#     if complete_sections is None:
#         return None
#     # remove metadata from the solution
#     strand_rebuilt = remove_meta_data(sections_num, complete_sections, frequency, letters_amount, read_size)
#
#     return strand_rebuilt
