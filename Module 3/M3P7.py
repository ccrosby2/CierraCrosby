# Cierra Crosby
# 1/31/2024
# This program asks for the starting day number, and the length of your stay.
# This program also tells you the number of the day in a week you will return on.
dayleave= int(input("What is day we leave?"))
daystay= int(input("What is the number of days we stay"))
triplength = daystay + dayleave
dayreturn = triplength%7
print("You return on day", dayreturn)