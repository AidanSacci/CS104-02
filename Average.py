#Aidan Sacci
#Average.py
total=0
average=0
howManyEntered=0
print("How many test scores would you like to average?")
howMany=int(input(''))
while howManyEntered<howMany:
    print("Enter test score:")
    testScore=float(input(''))
    total=total+testScore
    howManyEntered+=1
average=total/howMany
print("The average for the test scores you entered is:")
print(average)
