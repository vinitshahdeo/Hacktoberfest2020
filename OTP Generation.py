
import math, random 
  
# function to generate OTP 
def generateOTP() : 
  
    # Declare a digits variable   
    # which stores all digits  
    digits = "0123456789"
    OTP = "" 
  
   # length of password can be chaged 
   # by changing value in range 
    for i in range(4) : 
        OTP += digits[math.floor(random.random() * 10)] 
  
    return OTP 
  
while(1):
    p=input("Do you want to get a new OTP? (y/n) ")
    if(p=='y'):
        print("OTP of 4 digits:", generateOTP())
    else:
        print("Thank You")
        break
