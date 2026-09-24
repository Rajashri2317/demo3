
#college admission
state=str(input("enter your state name"))
marks=int(input("enter your marks"))
age=int(input("enter your age"))
qualification=input("enter your qualification")
if state.lower()=="karnataka":
    if marks>=50:
        if age>=18 and age<=25:
           if qualification=="10th pass": 
               print("admission eligible")
           else:
               print("admission cancelled due to failed qualification criteria")
        else:
            print("admission cancelled due to failed marks criteria")
    else:
        print("admission cancelled due to failed age criteria")
else:
    print("admission cancelled due to failed state criteria")

