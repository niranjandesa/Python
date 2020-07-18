import re


def longest_prefix():
    
    length=len(li)
    prefix_list=list()
    for i in range(length):
        for j in range(i+1,length):
            r= match(li[i],li[j])
            if r !='':
                prefix_list.append(r)
    return max(prefix_list)



def match(a,b):
    length=min(len(a),len(b))
    mat=""
    for i in range(length):
        if a[i]==b[i]:
            mat=mat+a[i]
        else:
            break
    return mat

if __name__=='__main__':
    li=['pea', 'pear', 'apple', 'for', 'april', 'apendix', 'peace']
    print(longest_prefix())
        
