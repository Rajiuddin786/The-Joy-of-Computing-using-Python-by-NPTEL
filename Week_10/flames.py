import string


def remove_matching_alphabet(l1:list,l2:list):
    for i in range(len(l1)-1):
        for j in range(len(l2)-1):
            if l1[i]==l2[j]:
                c=l1[i]
                l1.remove(c)
                l2.remove(c)
                l=l1+['*']+l2
                return [l,True]
    l=l1+['*']+l2
    return [l,False]

p1=input("Enter Name 1: ").strip().upper()
p2=input("Enter Name 2: ").strip().upper()

p1_list,p2_list=list(p1),list(p2)
proceed=True


while proceed:
    ret_list=remove_matching_alphabet(p1_list,p2_list)
    con_list=ret_list[0]
    proceed=ret_list[1]
    star_index=con_list.index('*')
    p1_list=con_list[:star_index]
    p2_list=con_list[star_index+1:]

count=len(p1_list)+len(p2_list)

result=['Friends','Love','Affection','Marriage','Enemy','Siblings']

while len(result)>1:
    split_index=(count%len(result)) - 1
    if split_index>=0:
        right=result[split_index+1:]
        left=result[:split_index]
        result=right+left
    else: result=result[:len(result)-1]

print(result[0])