ProjectScore=int(input("enter the project score:"))
InternalScore=int(input("enter the internal score:"))
ExternalScore=int(input("enter the external score:"))
if(ProjectScore>=50 and InternalScore>=50 and ExternalScore>=50):
    total_marks=ProjectScore*0.7+InternalScore*0.1+ExternalScore*0.2
    print(total_marks)
    if total_marks>=90:
        print("A grade")
    elif total_marks>80:
        print("B grade")
    else:
        print("C grade")
else:
    if ProjectScore<50:
        print("Failed in project, ProjectScore is:",ProjectScore)
    if InternalScore<50:
        print("failed in internals,Internals Score is:",InternalScore)
    if ExternalScore<50:
        print("failed in externals, Externals Score is:",ExternalScore)
    
