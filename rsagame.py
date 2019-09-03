import random

# Team Name, Round Score, Round Wins, Total Score, Playoff Status
teamsList = [[0,0,0,0,0],[1,0,0,0,0],[2,0,0,0,0],[3,0,0,0,0],[4,0,0,0,0],[5,0,0,0,0],[6,0,0,0,0],[7,0,0,0,0],[8,0,0,0,0],[9,0,0,0,0]]
rounds = 1
roundRup = 100

def printBoard():
    print('  _ _ _ _ _ _')
    for i in teamsList:
        tName = i[0]
        rPoints = i[1]
        rWins = i[2]
        print(str(tName)+' '+('X ') * (rPoints + rWins))

def printScores(round):
    print('At the end of Round #'+str(round)+', the scores are as follows:')
    for i in teamsList:
        tName = i[0]
        tPoints = i[3]
        rWins = i[2]
        print(str(tName)+' currently has '+str(tPoints)+' tournament points, and '+str(rWins)+' round wins!')
    input("Press enter to continue.")

def sortSecond(val):
    return val[3]

def standings():
    print(' ')
    print(' ')
    print(' ')
    print('At the end of the Regular Season, here are our standings:')
    teamsList.sort(key=sortSecond, reverse=True)
    for i in teamsList:
        print(str(i[0])+', with '+str(i[3])+' total points!')


while rounds < 5:
    availableRdPts = 10
    if roundRup < 10:
        teamsList[roundRup][1] += 1
        print(str(roundRup)+' scored 8 last round, and gets an extra point this round!')
        printBoard()
        roundRup = 100
    else:
        print('There was no prior team that scored 8!')
    while availableRdPts > 3:
        n = random.randint(0, 9)
        if (teamsList[n][1]+teamsList[n][2]) < 6:
            teamsList[n][1] += 1
            if teamsList[n][1]+teamsList[n][2] == 6:
                printBoard()
                input('\n'+str(n)+' is advancing. '+str(availableRdPts-1)+' points remain. Press enter to continue.')
                if availableRdPts > 8:
                    teamsList[n][2] += 1
                    teamsList[n][1] -= 1
                if availableRdPts == 8:
                    roundRup = n
                teamsList[n][3] += availableRdPts
                availableRdPts -= 1
    for i in teamsList:
        i[1] = 0
    print('')
    printScores(rounds)
    rounds += 1

input(standings())
playoffMatch14 = [teamsList[0],teamsList[3]]
playoffMatch23 = [teamsList[1],teamsList[2]]
print(' ')
print('Its going to be the #1 seeded '+str(playoffMatch14[0][0])+', with '+str(playoffMatch14[0][3])+' total points, going against the #4 seeded '+str(playoffMatch14[1][0])+', with '+str(playoffMatch14[1][3])+' total points.')
print('And, we will see the #2 seeded '+str(playoffMatch23[0][0])+', with '+str(playoffMatch23[0][3])+' total points, going against the #4 seeded '+str(playoffMatch23[1][0])+', with '+str(playoffMatch23[1][3])+' total points.')

championshipMatch = []
while True:
    input(printBoard())
    n = random.randint(0, 9)
    if n == playoffMatch14[0][0]:
        playoffMatch14[0][1] += 1
        if playoffMatch14[0][1]+playoffMatch14[0][2] == 6:
            print('Winner! '+str(playoffMatch14[0][0])+' is moving on!')
            championshipMatch += [playoffMatch14[0]]
            break
    elif n == playoffMatch14[1][0]:
        playoffMatch14[1][1] += 1
        if playoffMatch14[1][1]+playoffMatch14[1][2] == 6:
            print('Winner! '+str(playoffMatch14[1][0])+' is moving on!')
            championshipMatch += [playoffMatch14[1]]
            break

while True:
    input(printBoard())
    n = random.randint(0, 9)
    if n == playoffMatch23[0][0]:
        playoffMatch23[0][1] += 1
        if playoffMatch23[0][1]+playoffMatch23[0][2] == 6:
            print('Winner! '+str(playoffMatch23[0][0])+' is moving on!')
            championshipMatch += [playoffMatch23[0]]
            break
    elif n == playoffMatch23[1][0]:
        playoffMatch23[1][1] += 1
        if playoffMatch23[1][1]+playoffMatch23[1][2] == 6:
            print('Winner! '+str(playoffMatch23[1][0])+' is moving on!')
            championshipMatch += [playoffMatch23[1]]
            break

print(championshipMatch)
print('THE CHAMPIONSHIP MATCH! Its going to be '+str(championshipMatch[0][0])+' facing off against '+str(championshipMatch[1][0])+'!')
print('')

for i in championshipMatch:
    i[1] = 0

while True:
    n = random.randint(0, 9)
    if n == championshipMatch[0][0]:
        championshipMatch[0][1] += 1
        if championshipMatch[0][1]+championshipMatch[0][2] == 6:
            print('Winner! '+str(championshipMatch[0][0])+' is your Season Champion!')
            break
    elif n == championshipMatch[1][0]:
        championshipMatch[1][1] += 1
        if championshipMatch[1][1]+championshipMatch[1][2] == 6:
            print('Winner! '+str(championshipMatch[1][0])+' is your Season Champion!')
            break
