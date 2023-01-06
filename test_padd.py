from Improvement.Utilities import *

st = 'GCGCGGCGGCGGCGGCGGCGGCGGCGGCGGCGCGGACGTATGCCCGAGGGGCTGGGCGAAGGATTAGGCGATGCCAGCGCCGACCTGATTGCCGGAAGGT'
padding_hash = {132146444: ['ACTACTACTACTACTACTACTACTACTACT'], 228077107: ['CTTCTTCTTCTTCTTCTTCTTCTTCTTCTT'],
                456154214: ['TTGTTGTTGTTGTTGTTGTTGTTGTTGTTG'], 290335325: ['TGCTGCTGCTGCTGCTGCTGCTGCTGCTGC'],
                360223551: ['GCGGCGGCGGCGGCGGCGGCGGCGGCGGCG'], 95930663: ['CGACGACGACGACGACGACGACGACGACGA'],
                160732217: ['GATGATGATGATGATGATGATGATGATGAT'], 297965333: ['ATAATAATAATAATAATAATAATAATAATA'],
                158188881: ['TAGTAGTAGTAGTAGTAGTAGTAGTAGTAG']}

four_pow = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456,
            73741818,
            294967272, 179869082, 219476325, 377905297, 11621179, 46484716, 185938864, 243755453, 475021809, 400087227,
            100348899,
            401395596, 105582375, 422329500, 189317991, 257271961, 29087838, 116351352, 465405408, 361621623, 446486486,
            285945935,
            143783734, 75134933, 300539732, 202158922, 308635685, 234542734, 438170933, 252683723, 10734886, 42939544,
            171758176,
            187032701, 248130801, 492523201, 470092795, 380371171, 21484675, 85938700, 343754800, 375019194, 76767,
            307068,
            1228272, 4913088, 19652352, 78609408, 314437632, 257750522, 31002082, 124008328, 496033312, 484133239,
            436532947,
            246131779, 484527113, 438108443, 252433763, 9735046, 38940184, 155760736, 123042941, 492171764, 468687047,
            374748179,
            498992710, 495970831, 483883315, 435533251, 242132995, 468531977, 374127899, 496511590, 486046351,
            444185395,
            276741571, 106966278, 427865112, 211460439, 345841753, 383367006, 33468015, 133872060]


def find_full_padding(read, padding_size, paddings_hash, four_pow):
    temp_hash = full_hash(read=read, pos=0, length=padding_size)
    for pos in range(1, len(read) - padding_size + 1):
        if temp_hash in paddings_hash:
            if read[pos-1:pos-1 + padding_size] in paddings_hash[temp_hash]:
                return pos-1
        # check for pos+1
        # TODO: check if this is correct
        temp_hash = shift_right_hash(read, pos , padding_size, temp_hash, four_pow)
    return -1


print(find_full_padding(st, 30, padding_hash, four_pow))
