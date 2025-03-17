#convert L to ML
x = list(map(float, input().split()))  
a = [i * 1000 for i in x]  

for value in a:
    print(value, "ml")  



#get input from user store in array and display it
arr = list(map(int, input("Enter numbers: ").split()))
print("Stored array:", arr)


#correct program for above function
size = int(input("Enter the number of elements in the array:"))
array = [ ]
for i in range(size):
    element =  int(input("Enter element:"))
    array.append(element)

print (f"The array is:{array}")



