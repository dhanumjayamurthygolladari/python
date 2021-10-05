#python program for array left rotation
my_list=[11,22,16,13,18]
n=3
print("The list is : ")
for i in range(0, len(my_list)):
   print(my_list[i])

for i in range(0, n):
   first_elem = my_list[0]

   for j in range(0, len(my_list)-1):
      my_list[j] = my_list[j+1]

   my_list[len(my_list)-1] = first_elem

print()

print("Array after left rotating is : ")
for i in range(0, len(my_list)):
   print(my_list[i])
