first_names = ["James", "Anna", "Lucas", "Maria"]
last_names = ["Bond", "Skywalker", "Doe", "Smith"]

list_of_names = []


for first in first_names:
    
    col = []
   
    for last in last_names:
        
        col.append(first + " " + last)
    
    list_of_names.append(col)


print(list_of_names)
