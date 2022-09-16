import listhandle

def time_split(c):
    c = c.split(' \xa0 ')
    if c[-1][-1] == 'p':
        time_list = []
        b = c[-1].split('- ')
        b[-1] = b[-1].replace('p','')
        for i in b:
            i = i.split(':')
            time_list.append(i)
        if time_list[0][0] < time_list[1][0] and time_list[1][0] != '12':
            time_list[0][0] = str(int(time_list[0][0])+12)
            time_list[1][0] = str(int(time_list[1][0])+12)

        elif time_list[0][0] > time_list[1][0]:
            time_list[1][0] = str(int(time_list[1][0])+12)

        else:
            if time_list[0][0] != '12':
                time_list[0][0] = str(int(time_list[0][0])+12)
                time_list[1][0] = str(int(time_list[1][0])+12) 

            
    else:
        time_list = []
        b = c[-1].split('- ')
        for i in b:
            i = i.split(':')
            time_list.append(i)    
        
    return time_list

