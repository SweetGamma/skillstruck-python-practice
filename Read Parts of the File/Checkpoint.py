file = open("speech.txt", "r")


print(file.read(10))  


file.seek(0)
print(file.readline())  
print(file.readline()) 


file.close()
