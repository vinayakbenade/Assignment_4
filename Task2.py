file = open("output.txt", 'w')
writing_file =file.write(input("enter text to write to the file: "))
print("data successfully written to output.txt.")
file.close()

file = open("output.txt", 'a')
new_data =(input("enter additional text to append: "))
append_file =file.write('\n' + new_data)
print("data successfully appended.")
file.close()

file = open("output.txt", 'r')
reading_file = file.readlines()
if len(reading_file) >= 2:
    print("Final content of output.txt:")
    print(reading_file[0].strip())
    print(reading_file[1].strip())


