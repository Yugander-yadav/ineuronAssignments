# 1.What are the two values of the Boolean data type? How do you write them? 

# => Boolean has 2 possible value and they are written as  True,False


# 2. What are the three different types of Boolean operators?

#  Types of boolean operators :   and or not 


# 3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean
# values for the operator and what it evaluate ).

# AND Table 

#  X        Y            X and Y 
#  0        0               0
#  1        0               0
#  0        1               0
#  1        1               1


# OR Table 

#  X        Y            X or Y 
#  0        0               0
#  1        0               1
#  0        1               1
#  1        1               1


# not 

#  not(0)==> True / 1
#  not(1)==> False / 0




# 4. What are the values of the following expressions?


# (5 > 4) and (3 == 5) ==>               False
# not (5 > 4)           ==>              False
# (5 > 4) or (3 == 5)   ==>              True
# not ((5 > 4) or (3 == 5)) ==>          False
# (True and True) and (True == False)    False
# (not False) or (not True)     ==>      True


# 5. What are the six comparison operators?

#   <  > == != >= <=

# 6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.

# => Assignment operator is used to assign  value to an variable, where as equal to is an conditional operator 

# EXAMPLE :     a = "sample string " 
# Equal to :    print(1==1)




# 7. Identify the three blocks in this code:
spam = 0

if spam == 10:
    print("eggs")   #Block 1 
if spam > 5:
    print("bacon")  #Block 2 
else:
    print("ham")    #Block 3
    print("spam")
    print("spam")
    

# 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

spam = 1
if spam == 1:
    print("Hello")
if spam ==2:
    print("Howdy")
else:
    print(spam)
    
    

# 9.If your programme is stuck in an endless loop, what keys you’ll press?

#  ctrl + c 

# 10. How can you tell the difference between break and continue?

#  Break Statement : when break statement is used the execution of loop stops and control is exited from the loop 

# Continue Statement : when continue statement is used  the pirticular loop iteration is skipped to next iteration 


# 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10,1)
print("Question Number 11")


for i in range(10): # prints the value for 0 to 9 excluding 10 
    print(i)


for i in range(0,10): # prints the value for 0 to 9 excluding 10 
    print(i)

for i in range(0,10,1): # prints the value for 0 to 9 excluding 10  with incrementing  by 1 value 
    print(i)



# 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
# program that prints the numbers 1 to 10 using a while loop.

print("Question 12")

for i in range(1,11):
    print(i)

print("While loop")
i=1
while(i<11):
    print(i)
    i=i+1 


# 13. If you had a function named bacon() inside a module named spam, how would you call it after
# importing spam?

from spam import bacon;

bacon()

