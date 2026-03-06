# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

#removed '==' and changed it to '=' so that year becomes a variable , fixed int bracket and removing '.'
year = int(input("Greetings! What is your year of origin? "))         #fixed quotations 

if year <= 1900:                                     #added colen to fix  if statement
    print ("Woah, that's the past!")                 #fixed print statement by changeing ' to "
elif year >= 1900 and  year <= 2020:                          #fixed and statement
    print ("That's totally the present!")
else:                                                  #changed elif to else
    print ("Far out, that's the future!")
