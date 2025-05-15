
para2= "hello hello world hello hello world"
para_list= para2.split()
word_dict={}
for i in para_list:
    if i in word_dict:
        word_dict[i]+= 1
    else:
        word_dict[i]=1

print(word_dict)

