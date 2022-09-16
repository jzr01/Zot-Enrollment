import timehandle
import datehandle
import datahandle


#check if the class you choose is full
def check_status(combination_list):
    b = {1}
    for class_dict in combination_list:
        if class_dict != {}:
            if class_dict['Status'] == 'FULL':
                b.add('False')
            else:
                b.add('True')

    if 'False' in b:
        return False
    else:
        return True

#check if the class enroll have the co-required class enrolled
def check_corequire(combination_list,class_type_list1):
    b = {1}
    
    for i in range(0,len(combination_list),3):

        if class_type_list1[i//3] == ['Lec','Dis','Lab']:

            if combination_list[i+1] != {} and combination_list[i+2] != {} and combination_list[i] != {}:
            
                if combination_list[i+1]['Sec'].isnumeric() == True and combination_list[i+2]['Sec'].isnumeric() == True:
                
                    b.add('True')

                else:
                    if (combination_list[i]['Sec'] in combination_list[i+1]['Sec']) == True and (combination_list[i]['Sec'] in combination_list[i+2]['Sec']) == True:

                        b.add('True')

                    else:
                        b.add('False')

            elif combination_list[i+1] == {} and combination_list[i+2] == {} and combination_list[i] == {}:

                b.add('True')
                
            else:
                b.add('False')

        elif class_type_list1[i//3] == ['Lec','Dis']:
            
            if combination_list[i+1] != {} and combination_list[i] != {}:

                if combination_list[i+1]['Sec'].isnumeric() == True:
                    b.add('True')

                else:
                    if (combination_list[i]['Sec'] in combination_list[i+1]['Sec']) == True:

                        b.add('True')

                    else:
                        b.add('False')
            elif combination_list[i+1] == {} and combination_list[i] == {}:
                b.add('True')
            
            else:
                b.add('False')

        elif class_type_list1[i//3] == ['Lec','Lab']:

            if combination_list[i+2] != {} and combination_list[i] != {}:
            
                if combination_list[i+2]['Sec'].isnumeric() == True:
                    b.add('True')

                else:
                    if (combination_list[i]['Sec'] in combination_list[i+2]['Sec']) == True:

                        b.add('True')

                    else:
                        b.add('False')

            elif combination_list[i+2] == {} and combination_list[i] == {}:
                b.add('True')
                
            else:
                b.add('False')

        elif class_type_list1[i//3] == ['Lec']:

            b.add('True')
            
    if 'False' in b:
        return False

    else:
        return True

# check class time overlap

def time_not_overlap(time_interval1,time_interval2):

    b = {1}
    
    time_list1 = timehandle.time_split(time_interval1)
    time_list2 = timehandle.time_split(time_interval2)
    
    if time_list1[1][0] < time_list2[0][0]:
        b.add('True')

    elif time_list1[0][0] > time_list2[1][0]:
        b.add('True')

    elif time_list2[0][0] < time_list1[1][0]:
        b.add('False')
        
    elif time_list1[0][0] < time_list2[1][0]:
        b.add('False')
        
    elif time_list1[0][0] == time_list2[1][0]:

        if time_list1[1][1] <= time_list2[0][1]:
            b.add('True')

        else:
            b.add('False')
            
    elif time_list2[0][0] == time_list1[1][0]:

        if time_list2[1][1] <= time_list1[0][1]:
            b.add('True')
            
        else:
            b.add('False')

    if 'False' in b:
        return False

    else:
        return True

#check date overlap  

def date_not_overlap(date1,date2):
    b = {1}
    date_list1 = datehandle.date_handle(date1)
    date_list2 = datehandle.date_handle(date2)

    date_set1 = set(date_list1)
    date_set2 = set(date_list2)

    if date_set1.intersection(date_set2) == set():
        b.add('True')

    else:
        b.add('False')

    if 'False' in b:
        return False

    else:
        return True

def final_not_overlap(final1,final2):
    b = {1}
    if final1 != '    TBA' and final2 != '    TBA':
        if final1 != final2:
            b.add('True')
        else:
            b.add('False')
    else:
        b.add('True')

    if 'False' in b:
        return False

    else:
        return True

#check if time overlap

def check_time_time(combination_list):
    b = {1}
    for i in range(len(combination_list)-1):
        for j in range(i+1,len(combination_list)):
            if combination_list[i] != {} and combination_list[j] != {}:
                if time_not_overlap(combination_list[i]['Time'],combination_list[j]['Time']) == False:
                    if date_not_overlap(combination_list[i]['Time'],combination_list[j]['Time']) == False: 
                        b.add('False')
                    else:
                        b.add('True')
                
                else:
                    b.add('True')
                
            else:
                b.add('True')

    if 'False' in b:
        return False

    else:
        return True

def check_time_final(combination_list):
    b = {1}
    for i in range(len(combination_list)-1):
        for j in range(i+1,len(combination_list)):
            if combination_list[i] != {} and combination_list[j] != {}:
                if final_not_overlap(combination_list[i]['Final'],combination_list[j]['Final']) == True: 
                    b.add('True')
                else:
                    b.add('False')
                
            else:
                b.add('True')

    if 'False' in b:
        return False

    else:
        return True


def check_units(combination_list):

    total_unit = 0
    for element in combination_list:

        if element != {}:
            total_unit = total_unit + int(element['Units'])

        else:
            total_unit = total_unit

    if  16 <= total_unit <= 28:
        return True

    else:
        return False

