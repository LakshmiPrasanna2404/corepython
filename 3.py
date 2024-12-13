project=int(input("Enter project marks: "))
internal=int(input("Enter internal marks: "))
external=int(input("Enter external marks: "))

if project>50 and internal>50 and external>50:
    total_marks = (70/100)*project+(10/100)*internal+(20/100)*external
    if total_marks>90:
        print("A grade")
    elif 80<total_marks<90:
        print("B grade")
    else:
        print("C grade")
else:
    if project<50:
        print("Failed in project")
    if internal<50:
        print("Failed in internal")
    if external<50:
        print("Failed in external")






