u=[]
v=[]
au=[]
bv=[]
final=[]
sub=[]                  
n1=int(input("ENTER THE NO OF ELEMENT TO BE ENTERED IN BOTH U and V:"))
for i in range(n1):
    ele=int(input("ENTER THE ELEMENT FOR U: "))
    u.append(ele)
for i in range(n1):#true
    ele=int(input("ENTER THE ELEMENT FOR V: "))
    v.append(ele)
    
print("Element of vector U \n",u)
print("Element of vector v \n",v)
print ( "Menue") 
print ("1.vector scalar ")
print ("2.vector Addition")
print ("3.Dot product")
print ("4.subtraction")
print ("5.Exit")
i=0
while(i<4):
    
     choice=int(input(" Enter the choice you want to perform:"))
     if (choice==1):
       print("~~~You  choice Vector Sclar Lets beign~~~")
       a=int(input("Enter the element for  \n a(u):  "))
       b=int(input("Enter the element for  \n b(v):  "))
       for i in range (len(u)):
           mul=a*u[i]
           au.append( mul)
       print ("Scalar multipication of vector U with A : \n ",au)
       for i in range (len(v)):
           mult=b*v[i]
           bv.append(mult)
       print ("Scalar multipication of vector V with B : \n ",bv)

     elif (choice==2):
      
       for i in range (len(u)):
           Sum=u[i]+v[i]
           final.append(Sum)
       print ("Vector  Addition of vector AU with BV : \n ",final)
     elif(choice==3):
       p=[]
       for  i in range (len(u)):
            multipition=u[i]*v[i]
            p.append(multipition)
       print ("Vector  multipication of vector U with V: \n ",p)
       dot=0
       for i in range (len(p)):
           dot=dot+p[i]
       print("Dot product of U and V: \n ",dot)

     elif(choice==4):
        
          for i in range (len(u)):
              Subt=u[i]-v[i]
              sub.append(Subt)
          print ("Vector  subtraction of vector AU with BV : \n ",sub)
     elif(choice==5):
          break
     else:
          print ("~~~~Iput Validation~~~~~~~~")
            
     print(i)
           
        
            

        




        
        
