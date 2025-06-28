import math
print("be barname mashin hesab khosh amadid..")
print("baray bealave (+)vard konid \n tafrigh..( - ) \n zarb..( * )\n taghsim..( / ) \n darsad..( % ) \n sinos..( sin )\n tavan..( ** )\n v baray khorog as barname horof..( D ) vard konid.! ")
def plus1():
     print("salam in barname baray (+++) ast")
     x = int(input("enter the first number"))
     y = int(input("enter the second number"))
     a = int(input("enter the therd number"))
     z = (x+y+a)
     print (z)

          
def mines1():
     print("salam in barname baray (---) ast")
     x = int(input("enter the first number"))
     y = int(input("enter the second number"))
     a = int(input("enter the therd number"))
     z = (x-y-a)
     print (z)
    
    
def zarb1():
     print("salam in barname baray (xxx) ast")
     x = int(input("enter the first number"))
     y = int(input("enter the second number"))
     a = int(input("enter the therd number"))
     z = (x*y*a)
     print (z)
 
def taghsim():
     print("salam in barname baray (///) ast")
     x = int(input("enter the first number"))
     y = int(input("enter the second number"))
     a = int(input("enter the therd number"))
     z = (x/y/a)
     print (z)     
    
    
def percent1():
 while 1:    
     x = int(input("enter the total price :"))
     if x<=0:
          print ("plase enter corect price..!")
          continue
     y = float(input("enter the percent : "))
     z = (x*y)/100
     print (z)
     
     
     
def sin():
     x = int(input("enter the number for sin :"))
     z = math.sin(x)
     print(z)
  

def tavan():
  x = (int(input("adad paye shoma chand ast..?")))
  z = (int(input("tavan chand mikhayd ..?")))
  while 1:
       if z < 0:
           print("dorost vared konid" )
           continue
       else:
           y = (pow(x,z))
           print(x, "be tavan 2 mishe .." , y) 
           break


def karbar():
   while 1: 
    anjam_kar =input("che kari mikhay anjam bedam..?")
    if anjam_kar =="+":
         plus1()
    elif anjam_kar =="-":
         mines1()
    elif anjam_kar =="/":
         taghsim()
         
    elif anjam_kar =="sin":
         sin()
         
    elif anjam_kar =="*":
         zarb1()
         
    elif anjam_kar =="**":
         tavan()
    elif anjam_kar =="%":
         percent1()
    elif anjam_kar =="D":
         break    
    else:
         print("lotfan horof dorost ro vared konid..!")
         continue
karbar()    
             