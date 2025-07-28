content = "how are you bro!"  # Content to write

with (
    open('file1.txt', 'w') as f1,
    open('file2.txt', 'w') as f2
):
    f1.write(content.upper())  # Write uppercase version to f1
    f2.write(content.lower())  # Write lowercase version to f2