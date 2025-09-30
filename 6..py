x=int((input("cislo x: ")))
z=x%4
y=x%7

if z==0 and y==0:
    print("cislo je delitelne 4 aj 7")
if z==0 and y!=0:
    print("cislo je delitelne len 4")
if z!=0 and y==0:
    print("cislo je delitelne len 7")
if z!=0 and y!=0:
    print("cislo je nie je delitelne ani 4 ani 7" )