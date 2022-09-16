import re

# set a function to get course name
def getname(class_name_rawdata):

    #get the class name
    
    a = class_name_rawdata[0]
    a = re.split(' +',a)
    if a[0] == 'I&C':

        return a[0]+' '+a[1]+' '+a[3]

    else:

        return a[0]+' '+a[2]
