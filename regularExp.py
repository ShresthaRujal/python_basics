import re

patterns = ['rujal','shrestha']
text = "Hello i am rujal Shrestha. i am a developer"

email = "rujal@sys.ai"
split_term = '@'
print(re.split(split_term,email))
print(re.findall("a",text))

for pattern in patterns:
    print("Searching: "+pattern)

    if re.search(pattern,text):
        print("Match")
    else:
        print("No Match")
