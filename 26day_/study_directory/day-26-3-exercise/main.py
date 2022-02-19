file_1_txt = open("file1.txt")
file1 = file_1_txt.read().splitlines()

file_2_txt = open("file2.txt")
file2 = file_2_txt.read().splitlines()

result = [int(i) for i in file1 if i in file2]

# Write your code above 👆
print(result)
file_1_txt.close()
file_2_txt.close()


