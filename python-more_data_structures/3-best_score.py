#!/usr/bin/python3
def best_score(a_dictionary):
    values = []
    l_num = None
    if not a_dictionary:
        return None
    for k, v in a_dictionary.items():
        values.append(v)
        srt = sorted(values)
        l_num = srt[-1]
    for k, v in a_dictionary.items():
        if l_num == v:
            return k