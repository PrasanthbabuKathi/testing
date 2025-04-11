# preprocess.py
print("Step 1: Preprocessing data...")
filename = "data.txt"
with open(filename, "w") as f:
    f.write("processed data")
print("Step 1 is compleated and created the file")
try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File Content:\n")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
