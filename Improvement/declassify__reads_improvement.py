from Improvement.Utilities import *

NO_FULL_PADDING = -1


def find_repetitive_letters(read, letters_amount, frequency, classifications):
    for i in range(0, frequency + letters_amount):
        candidate = read[i: i + letters_amount]
        if candidate not in classifications:
            continue
        was_repetitive = True

        for j in range(i + frequency + letters_amount, len(read), frequency + letters_amount):
            # TODO: check if splitting the read first can reduce time instead of copying
            temp = read[j:j + letters_amount]

            if len(temp) != len(candidate):
                break
            if temp != candidate:
                was_repetitive = False
                break

        if was_repetitive:
            return candidate
    return ""


# TODO: check for this function
def find_full_padding(read, padding_size, paddings_hash, four_pow):
    temp_hash = full_hash(read=read, pos=0, length=padding_size)
    for pos in range(0, len(read) - padding_size):
        if temp_hash in paddings_hash:
            if read[pos:pos + padding_size] in paddings_hash[temp_hash]:
                return pos
        # check for pos-1
        temp_hash = shift_right_hash(read, pos - 1, padding_size, temp_hash, four_pow)
    return NO_FULL_PADDING


def is_padding_at_start(read, letters_amount, freq):
    padding_partial = read[0:letters_amount+1] * (freq // (letters_amount+1))
    padding_partial += read[0:freq % (letters_amount+1)]
    return padding_partial == read[0:freq]


def declassify_with_padding(read, freq, padding_size, paddings_hash, letters_amount):
    # can be two cases: either the padding is somewhere in the middle, in which case it is in full length,
    # or it will be partially cut in the beginning or the end.
    # If it's in the middle,
    # we'll check if every padding_length combo of letters is one of possible paddings in the next function:
    padding_start = find_full_padding(read, freq, padding_size, paddings_hash)

    if padding_start != NO_FULL_PADDING:
        return read[padding_start: padding_start + letters_amount], (True, padding_start)
    # otherwise, the padding is partial and in either the beginning or the end
    else:
        is_at_start = is_padding_at_start(read, letters_amount, freq)

        if is_at_start:
            return read[0:letters_amount + 1], (False, 0)
        else:
            return read[-letters_amount - 1:], (False, -1)



if __name__ == '__main__':
    pass
