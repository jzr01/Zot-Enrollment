#This function is used to convert tuple in the product to list
def listconvert(raw_list):
    my_list = []
    for ele in raw_list:
        ele = list(ele)
        my_list.append(ele)

    return my_list 

output = []
def reemovNestings(l):
    for i in l:
        if type(i) == list:
            reemovNestings(i)
        else:
            output.append(i)
    return output


def flatten_list(a):
    output.clear()
    return reemovNestings(a)
