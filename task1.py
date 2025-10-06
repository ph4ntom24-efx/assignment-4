try:
    with open("sample.txt") as file:
        for i,line in enumerate(file,start=1):
            print(f"row {i}. {line.strip()}")
except FileNotFoundError:
    print("ERROR: file dose not exist")