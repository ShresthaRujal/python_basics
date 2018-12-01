try:
    f = open("simple.txt","w+")
    f.write("Hello rujal")
except IOError:
    print("ERROR: Could not find file")
else:
    print("Success")
    f.close()
