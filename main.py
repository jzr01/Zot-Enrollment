import enrollment
import datahandle
import listhandle
import condition
import timehandle

if __name__ == '__main__':
    a = 'classes.csv'
    b = datahandle.class_info_rawdata(a)

    c = datahandle.class_name_index_list(b)
    d = datahandle.class_name_raw_list(b)
    e = datahandle.class_name_list(d)
    f = datahandle.class_dict_list(a,b,c,d)
    g = datahandle.class_final_list(e,f)
    h = datahandle.class_type_list(g)
    i = enrollment.Autoenroll(h,g)

