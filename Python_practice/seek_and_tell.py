with open("myfile.txt", "r") as f:
    f.seek(11)
    print(f"This is the position of seeked character : {f.tell()}")
    data = f.read(5)
    print(data)