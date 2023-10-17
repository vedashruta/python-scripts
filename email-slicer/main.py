file = input("Enter File Name : ")
try : 
    fileobj = open(file, "r")
    out_file = open("output.txt","w")
    lines = fileobj.readlines()

    for line in lines:
        if line == "\n" :
            continue
        else:
            line.strip()
            user_name = line[:line.index("@")].strip()
            domain = line[line.index("@")+1:].strip()
            format_ = f"Username : {user_name}\nDomain   : {domain}"
            # print("Username : "{}"\n Domain : {}".format(user_name,domain))
            out_file.writelines(format_+"\n")
            #print(format_)
    fileobj.close()
    out_file.close()
except IOError:
    print("File not found!!")    