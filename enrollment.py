import listhandle
import itertools
import condition
import datahandle
import getname

def Autoenroll(class_type_list1,class_final_list1):
    i = 1
    e = 0
    b = class_final_list1[0]
    choice_list = []
    while i < len(class_final_list1):
        b = listhandle.listconvert(list(itertools.product(b, class_final_list1[i])))
        i = i + 1
    for element in b:
        element = listhandle.flatten_list(element)
        

        if condition.check_status(element) == True:

            if condition.check_corequire(element,class_type_list1) == True:
                
                if condition.check_time_time(element) == True:
                   
                    if condition.check_units(element) == True:
                        e = e + 1
                        print('Choice'+ str(e) +':')
                        for ele in element:
                            if ele != {}:
                                print(ele["Code"]+' '+ele["Name"]+' '+ele["Sec"]+' '+ele["Time"])
                        print('--')
                    
                            
                            
                        
                    
    return None




    
