# TODO: Open the file "students.txt" in read mode
with open("students.txt", "r") as file:  # 'r' mode opens the file for reading

    # TODO: Read the file content (use the correct file method)
    content = file.read()  # Use the 'read()' method to get the entire content as a string

# TODO: Print the content of the file
    print(content)
