def read_file(file_name):
    f = open(file_name,"r")
    file_content = f.read()
    f.close()
    print(file_content)
    return file_content