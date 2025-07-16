"""write file"""
book={}
book['tom']={
    'name':'tom',
    'address':'1 red street NY',
    'phone':785169
}
book['bob']={
    'name':'bob',
    'address':'1 green street NY',
    'phone':7984678
}

import json
s=json.dumps(book)
# print(s)
with open ("C://Users//ashis//OneDrive//Desktop//python//book.txt","w")as f:
    f.write(s)


"""read file """
f= open ("C://Users//ashis//OneDrive//Desktop//python//book.txt","r")
s=f.read()
print(s)



