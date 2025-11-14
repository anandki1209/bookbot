def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def count_occurence(text):
    occurence = {}
    for c in text.lower():
        if c in occurence:
            occurence[c] += 1
        else:
            occurence[c] = 1
    return occurence


def sort_on(items):
    return items["num"]


def sort_dict(items):
    dict_list = []
    for i in items:
        dict_list.append({"char": i, "num": items[i]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


    
