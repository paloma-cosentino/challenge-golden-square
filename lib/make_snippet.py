def make_snippet(string):
    list_string = string.split()
    if len(list_string) <= 5:
        return string
    else:
        shortened_list = list_string[0:5]
        shortened_string = " ".join(shortened_list)
        final_string = f"{shortened_string} ..."
        return final_string