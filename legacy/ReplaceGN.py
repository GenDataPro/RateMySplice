import re
from operator import itemgetter
#seq = input ('Enter sequence: ')

seq ="cacacgtccgccggccctcagagcccgagcgacttccgccccaggccaccgtccacccgcagaaacgcgccgacccacactccgcagacaggaaccctcgggagtccccgctgatgaagtaccgacaggagatggcacgcgccgggagagagtcccaagaagggagaacctcgcgttcgcacactccaggcagcaccgagcagccgacaaaatcgcccatcacatctccgtcgcagatcctatcgatttcgttcgagaaggacaagcctcctgagcagcccccgccccaggggggccagggtcctcttacagcagccaacctcatcgatgccatcatcactcaccagataaactcgtcggccacgatatcgggtgacaacagaaaggagtcgtcaaatgattcacaagacagcgcctcgcgcgtccctccccgaggccgcgtgtcccccgcgccgcgcccgagccacacacccctgcagggagagggagggcgaatccgcgcccccgtgtggcagcttcccgaggccgaccacgggtcgtcgcgggaacaacagcagaaccacgggcggagggagagtcaggagagctcgtcccaggagggtcctcccgggaaccactacgggccggggagaaacaccgcccacgccgacagcaccaccaacagggcgacgaaagtgcagcagatcaccctgggcgagcacatctcaaatatcatccaccaagactacagccagaggcctggccagaacccaagcccagcgcccaatcctttacatcgtccgcagtcgacctccagcctgagccggtccccggcggcaaaggaaagggaggcggccatgcagaggtcacggactccggacgcgcgctgcagctctgactcctccaggagcaacatcgacgtggagccgatctctccgccagccggcgacagccaggactcgcagcccggctcggagcagtggcagccgcgcccgcaggacgtcccccccagaagccaacagcagcagcagcctccgtacggtcgtccacctcccagcgggcccggcgctggccaggcttggggtggaggggccaaacgttcatcccctagagtcggcaccaacctggaggacatcatccgcaaggctctgatgggagatgatgaggagaatgagggggatcctcctcctcagcagcaacagcagcccaggccgagctccacccactcctacgggcagcagatccaccaggtctcctctgcgtcatccccgagggacggctcgatgcagagccgcatcctgcgccagcgcaacgacagcgagacggagaccgagtcggaaacggagaccaaagaggcccccgtggcagaccggagccggtcgccacgcagctaccctccgaagaagaagcacaccatgtccgaggtggcttccccgcgcggccgcccggatatgcctggtccaccagacatgtcagcggcgcagaaagcggagatgggagcaggcgggcggttgccgtccacaggcagtgaacgctccaggctatccagcgcagccacgcctcctcggtccagccctcgcccttcctccgccgacgcaccgagcgcgtcctatcccttctcggcgctcttcctgaggggatccatgggcccgtcctcatcccctctccctccaacctcctccgcaacacaacagggtctgcccccgacgtccggtggcgagatcgcccacgaagccgcgcagaggacagccccgtccccggccacctcagcccgacacgacggcgagccggcgcctctgttgtcatcccagtacgagcctctgtccgacaccgatgaggaatcatga"

l = ['ga','gc','gg']

[i.start() for i in re.finditer('ga', seq)]
seqx = {s:[{"sequence":seq[index-3:index+6], "start_index":index-3, "end_index":index+6} for index in [i.start() for i in re.finditer(s, seq)]] for s in l}


modified_sequences = []
for pair, sequences in seqx.items():
    for sequence in sequences:
        modified_sequence = sequence.copy()
        if len(sequence["sequence"]) == 9:
            if sequence["sequence"][3:5] == pair:
                modified_sequence["sequence"] = sequence["sequence"][0:3]+"gt"+sequence["sequence"][5:9]
            modified_sequences.append(modified_sequence)
        else:
            print("Invalid sequence\n")
            print(sequence)

sorted_sequences = sorted(modified_sequences, key=itemgetter("start_index"))

output_text = []

for sequence in sorted_sequences:
    sequence_text = "\n>{start_index}to{end_index}\n{sequence}\n".format(**sequence)
    output_text.append(sequence_text)

f = open("Replace.txt", "w")
for text in output_text:
    f.write(text)
f.close()
