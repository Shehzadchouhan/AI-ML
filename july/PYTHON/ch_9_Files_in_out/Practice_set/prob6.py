word="python"
with open("logfile.txt", "r") as f:
    content=f.read()

    if word in content:
        print("Word found in the file.")
    else:
        print("Word not found in the file.")

f.close()