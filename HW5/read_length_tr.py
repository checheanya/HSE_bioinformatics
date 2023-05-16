def run_length_encoding(seq):
    result_names = list()
    result_counts = [1]
    i = 0
    while i < len(seq)-1:
        result_names.append(seq[i])
        result_counts.append(1)
        if seq[i] == seq[i+1]:
            while seq[i] == seq[i + 1]:
                result_counts[-1] += 1
                i += 1
        i += 1

    return result_names, result_counts

Read='AACTTGTGGAATTTGTTGAGAAA$'

print(run_length_encoding(Read))