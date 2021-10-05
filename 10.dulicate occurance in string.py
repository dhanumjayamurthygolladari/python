test_string = 'kavi is a girl. kavi is beautiful in looking  , looking her daily is enough.'
  
print("The original string is : " + str(test_string))
replace_dict = {'kavi' :  'She', 'looking' : 'that' }

test_list = test_string.split(' ')
r = set()
for i, el in enumerate(test_list):
    if el in replace_dict:
        if el in r:
            test_list[i] = replace_dict[el]
        else:
            r.add(el)
r = ' '.join(test_list)
  
# printing result 
print("The string after replacing : " + str(r)) 
