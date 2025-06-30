import math
print("be barname mashin hesab khosh amadid..")
print("baray bealave (+)vard konid \n tafrigh..( - ) \n zarb..( * )\n taghsim..( / ) \n darsad..( % ) \n sinos..( sin )\n tavan..( ** )\n v baray khorog as barname horof..( D ) vard konid.! ")
def plus1():
     print("salam in barname baray (+++) ast")
     while 1: 
        try:
         x = int(input("enter the first number:"))
         y = int(input("enter the second number:"))
         a = int(input("enter the therd number:"))
        except ValueError:
           print("plase enter corect number..!")
           continue
        z = (x+y+a)
        print (z)
        done_or_not=input("for plus again write (A) for exit(E):")
        if done_or_not =="A" or "a":
           continue         
        else:
            break
def mines1():
     print("salam in barname baray (---) ast")
     while 1:
      try:    
       x = int(input("enter the first number:"))
       y = int(input("enter the second number:"))
       a = int(input("enter the therd number:"))
       
      except ValueError:
           print("plase enter corect number..!")
           continue
      z = (x-y-a)
      print (z)
      done_or_not=input("for mines again write (A) for exit(E):")
      if done_or_not == "A" or "a":
           continue
      else :
           break
    
    
def zarb1():
     print("salam in barname baray (xxx) ast")
     while 1:
      try: 
       x = int(input("enter the first number:"))
       y = int(input("enter the second number:"))
       a = int(input("enter the therd number:"))
      except ValueError:
           print("plase enter corect number..!")
           continue
      z = (x*y*a)
      print (z)
      done_or_not=input("for zarb again write (A) for exit(E):")
      if done_or_not == "A" or "a":
           continue
      else :
            break
 
def taghsim():
     print("salam in barname baray (///) ast")
     while 1: 
      x = int(input("enter the first number:"))
      y = int(input("enter the second number:"))
      a = int(input("enter the therd number:"))
      z = (x/y/a)
      print (z)     
      done_or_not=input("for plus again write (A) for exit(E):")
      if done_or_not == "A" or "a":
           continue
      else :
           break
    
def percent1():
 while 1:
     try:     
      x = int(input("enter the total price :"))
      y = float(input("enter the percent : "))
     except ValueError:          
          print("plase enter corect number..!")
          continue
     if x<=0:
          print ("plase enter corect price..!")
          continue
     z = (x*y)/100
     print (z)
     done_or_not=input("for pecent again write (A) for exit(E):")
     if done_or_not == "A" or "a":
           continue
     else :
           break
     
     
def sin():
     while 1:
      try:
           x = int(input("enter the number for sin :"))
      except ValueError:
           print("plase enter corect number..!")
           continue
      z = math.sin(x)
      print(z)
      done_or_not=input("for sin again write (A) for exit(E):")
      if done_or_not == "A" or "a":
           continue
      else :
           break
  

def tavan():
  while 1: 
    try:
       x = (int(input("adad paye shoma chand ast..?")))
       z = (int(input("tavan chand mikhayd ..?")))
       
    except ValueError:
       print("plase enter corect number..!")
       continue
    if z < 0 :
        print("dorost vared konid" )
        continue
    else:
        y = (pow(x,z))
        print(x, "be tavan 2 mishe :" , y) 
     
    done_or_not=input("for plus again write (A) for exit(E):")
    if done_or_not == "A" or "a":
           continue
    else :
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
             
