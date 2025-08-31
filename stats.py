def get_num_words(text):
    num_words = len(text.split(" "))
    return num_words

def get_num_char(text):
    lowercase = text.lower()
    mapping = {}
    for el in lowercase:
        if el not in mapping:
            mapping[el] = 0
        mapping[el] += 1

    return mapping

def get_sorted_char(char_counts):
    counts = []
    for key, value in char_counts.items():
        counts.append({
            "char": key,
            "num": value
        })
    
    counts.sort(reverse=True, key=lambda x: x["num"])
    return counts