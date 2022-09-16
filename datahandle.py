import csv
import getname
import listhandle
import itertools

#1.1 Define initial data
def class_info_rawdata(a):

    class_info_rawdata = []

    with open(a,'r',newline='') as myfile:
        data = csv.reader(myfile)
        for row in data:
            if row[0] != '' and row[0] != 'Name' and row[0] != 'Code':
                class_info_rawdata.append(row)
    return class_info_rawdata

def class_name_rawdata(a):
    class_name_rawdata = []
    with open(a,'r',newline='') as myfile:
        data = csv.reader(myfile)
        for row in data:
            if row[0] != '' and row[1] == '':
                class_name_rawdata.append(row)
    return class_name_rawdata

def class_info_key_list(a):
    class_info_key_list = []
    with open(a,'r',newline='') as myfile:
        data = csv.reader(myfile)
        for row in data:
            if row[0] == 'Code' and row[1] == 'Type':
                class_info_key_list.append(row)
    return class_info_key_list
            

#2. create the class dictionary

def get_the_key(a):
    class_info_key_list = []
    with open(a,'r',newline='') as myfile:
        data = csv.reader(myfile)
        for row in data:
            if row[0] == 'Code' and row[1] == 'Type':
                class_info_key_list.append(row)
        class_info_key_list = class_info_key_list[0]
        class_info_key_list.reverse()
        class_info_key_list.append('Name')
        class_info_key_list.reverse()
    return class_info_key_list

def class_name_index_list(class_info_rawdata1):
    class_name_index_list = []
    for element in class_info_rawdata1:
        if element[0].isnumeric() == False and element[0] != 'Code' and element[0] != 'Name':
            class_name_index_list.append(class_info_rawdata1.index(element))
    class_name_index_list.append(len(class_info_rawdata1))
    return class_name_index_list


class_info_list = []
def class_name_raw_list(class_info_rawdata1):
    class_name_raw_list = []

    for element in class_info_rawdata1:

        if element[0].isnumeric() == False:
            if element[0] !='Code' and element[0] != 'Name':
                class_name_raw_list.append(element)

    return class_name_raw_list


# 2.3 build a name_list
def class_name_list(class_name_raw_list1):
    class_name_list = []
    for element in class_name_raw_list1:
        class_name_list.append(getname.getname(element))

    return class_name_list


# 2.4 build the class dictioanry
def class_dict_list(a,class_info_rawdata1,class_name_index_list1,class_name_raw_list1):
    class_dict_list = []

    for i in range(len(class_name_index_list1)-1):   
        for j in range(class_name_index_list1[i]+1,class_name_index_list1[i+1]):
            my_dict = {}
            for m in range(len(class_info_rawdata1[j])+1):
                if m == 0:
                    my_dict[get_the_key(a)[m]] = getname.getname(class_name_raw_list1[i])                
                else:
                    my_dict[get_the_key(a)[m]] = class_info_rawdata1[j][m-1]
            class_dict_list.append(my_dict)
    return class_dict_list

#3.1 divide in to different list base on class
def class_final_list(class_name_list1,class_dict_list1):
    class_type = ['Lec','Dis','Lab']
    class_final_list = []

    for name in class_name_list1:
        for types in class_type:
            class_type_list = []
            for element in class_dict_list1:
                if element['Name'] == name and element['Type'] == types:
                    class_type_list.append(element)

            class_type_list.append({})
            class_final_list.append(class_type_list)

    return class_final_list

#3.2 build a dictionary to tell how many class type are there for each class
def class_type_list(class_final_list1):
    class_type_list = []
    for i in range(0,len(class_final_list1),3):
        type_list = ['Lec','Dis','Lab']
        for j in range(i,i+3):
            if class_final_list1[j][0] == {}:
                if j%3 == 0:
                    type_list.pop(0)
                elif j%3 == 1:
                    type_list.pop(1)
                else:
                    type_list.pop(2)
    
        class_type_list.append(type_list)

    return class_type_list






















