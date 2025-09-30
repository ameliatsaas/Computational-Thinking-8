twilightcore = 0
aestheticfall = 0
halloweencore = 0


answer = input ("On a fall weekend would you rather A) go on a walk in the woods, B)go to a cafe, C)go to a pumpkin patch or farm, or D) watch spooky movies")
if answer == "A":
    twilightcore += 1
elif answer == "B":
    aestheticfall += 1
elif answer == "C":
    aestheticfall += 1
    halloweencore += .5
elif answer == "D":
    halloweencore += 1
else:
    print("please choose A, B, C, or D")


answer = input ("Pick a song, A) Duvet by Boa, B) There She Goes by the La's, C) People are Strange by The Doors, D) tis the damn season by Taylor Swift, or B) Rhiannon by Fleetwood Mac")
if answer == "A":
    twilightcore += 1
elif answer == "B":
    aestheticfall += 1
elif answer == "C":
    halloweencore += 1
elif answer == "D":
    twilightcore += 1
elif answer == "E":
    halloweencore += 1
else:
    print("please choose A, B, C, D, or E")

answer = input ("Pick a fall scent, A) woods, lavender, and smoke, B) coffee, vanilla, and pumpkin, or C) leather, sugar, and amber")
if answer == "A":
    twilightcore += 1
elif answer == "B":
    aestheticfall += 1
elif answer == "C":
    halloweencore += 1
else:
    print ("please choose A,B or C")


answer = input ("How do you like to decorate for fall? A) spooky halloween decorations, B) autumn and harvest themed decor, or C) you don't really like to decorate")
if answer == "A":
    halloweencore += 1
elif answer == "B":
    aestheticfall += 1
elif answer == "C":
    twilightcore += 1
else:
    print("please choose A, B or C")


answer = input ("A)Coke or B)Pepsi? (or C)Dr Pepper)")
if answer == "C" or answer == "c":
    halloweencore += 1
    aestheticfall += 1
    twilightcore += 1
elif answer == "B" or answer == "b":
    halloweencore +=1
    aestheticfall += 1
    twilightcore += 1
elif answer == "A" or answer == "a":
    twilightcore += 1
    aestheticfall += 1
    halloweencore += 1
else:
    print ("check your spelling")


if twilightcore>aestheticfall and twilightcore>halloweencore:
    print("Your aesthetic is twilightcore(aka vintage, dark,Y2K autumn)")
elif aestheticfall>twilightcore and aestheticfall>halloweencore:
    print("Your aesthetic is classic fall(aka gilmore girls, cozy, and aesthetic autumn)")
elif halloweencore>aestheticfall and halloweencore>twilightcore:
    print("Your aesthetic is halloweencore(aka spooky or scary fall)")


print("Thanks for taking my quiz!")