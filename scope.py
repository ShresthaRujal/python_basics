#global
name = "this is global"

def greet():
    
    name = "sammy"
    #if want to change global value then use 'global' keyword as
    #global name
    #name = "name"
    def hello():
        print("Hello "+ name)

    hello()

greet()
print(name)
