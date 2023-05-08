def comma_and(list_value):
    if len(list_value) == 0:
        return ""
    elif len(list_value) == 1:
        return str(list_value[0])
    else:
        return ', '.join(map(str, list_value[:-1])) + ' and ' + str(list_value[-1])
    
list1 = ['python','php','sql','js','C']
print(comma_and(list1))