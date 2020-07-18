''' This is utility module '''


def rotate(li,offset=[]):
    try:
       li=list(li)
    except TypeError as err:
        return f'Error: {err}'
    temp=li.copy()
    first_element=temp[0]
    temp.remove(first_element)
    temp.append(first_element)
    return offset+temp

def to_str(li):
    temp=""
    try:
        for i in li:
            temp = temp + i
        return temp
    except (TypeError,ValueError) as err:
        return f'Error: {err}'
