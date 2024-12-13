Basic=int(input("Enter salary:"))

if(Basic<10000):
    HRA=(67/100)*Basic
    DA=(73/100)*Basic
elif(Basic>10000 and Basic<20000):
        HRA = (69/100)*Basic
        DA = (76/100)*Basic
else:
        HRA = (73/100)*Basic
        DA = (89/100)*Basic
GS=HRA+DA+Basic
print(f"Gross Salary:{GS}")