def date_handle(c):
    c = c.split('   ')
    date_dict= ['M','Tu','W','Th','F']
    date_list = []
    for i in date_dict:
        if i in c[0]:
            date_list.append(i)

    return date_list

