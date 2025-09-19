#Write a program to calculate the number of notes in the given amount?
#100,50,10 rupees
total = int(input("How many rupees? "))
hundreds = total//100
money_left1 = total - (hundreds * 100)
fifties = money_left1//50
money_left2 = money_left1 - (fifties *50)
tens = money_left2//10
money_left3 = money_left2 - (tens*10)
remainder = money_left3
print("These rupees can be split into " + str(hundreds) + " hundreds, " + str(fifties) + " fifties, and " + str(tens) + " tens. Your remaining rupees will be " + str(remainder) + ".")