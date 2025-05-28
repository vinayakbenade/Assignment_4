try:
    with open("sample.txt", "r") as file:
        lines = file.readlines()
        if len(lines) >= 2:
            print("Line 1:", lines[0].strip())
            print("Line 2:", lines[1].strip())
        else:
            print("Error: The file does not have enough lines.")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
