result=""; 
for row in range(0,7):
    for col in range(0,7):
        if(((col==0 or col==4) and row!=0 ) or ((row==0 or row==3) and (col>0 and col<4))):
            result=result+"*"
        else:
            result=result+" "   
    result=result+"\n"
print(result); 

