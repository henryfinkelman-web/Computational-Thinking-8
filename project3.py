# personalty quiz
jsn_points = 0
puka_points = 0 
amonra_points = 0

answer1 = input (" do you perfer A speed B catching C size")
if answer1 == "A":
    jsn_points += 1
elif answer1 == "B":
    amonra_points +=1 
elif answer1 == "C":
    puka_points +=1 

answer2 = input (" do you perfer A number 11 B number 14 C number 12") 
if answer2 == "A":
    jsn_points += 1
elif answer2 == "B":
    amonra_points +=1
elif answer2 == "C":
    puka_points +=1

answer3 = input (" do you perfer A seahawks B lions C Rams") 
if answer3 == "A":
    jsn_points += 1
elif answer3 == "B":
    amonra_points +=1
elif answer3 == "C":
    puka_points +=1

answer4 = input (" do you perfer A ohio state B USC C BYU") 
if answer4 == "A":
    jsn_points += 1
elif answer4 == "B":
    amonra_points +=1
elif answer4 == "C":
    puka_points +=1

answer5 = input (" do you perfer A the city of seattle B the city of deteriot C the city of La") 
if answer5 == "A" or answer5 == "a":
    jsn_points += 1
elif answer5 == "B":
    amonra_points +=1
elif answer5 == "C":
    puka_points +=1

# end of quiz:
if jsn_points > puka_points and jsn_points > amonra_points:
    # you will get thie ending if jsn has the most points
    print (" Looks like you think jsn is the best")
elif amonra_points > puka_points and amonra_points > jsn_points:
    # you will get thie ending if amonra has the most points
    print (" looks like you think amonra is the best")
elif puka_points > jsn_points and puka_points > amonra_points:
    # you will get thie ending if puka has the most points
    print (" Looks like you think puka is the best ")