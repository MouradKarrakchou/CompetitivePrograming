numberOfPerson, numberOfConnection = list(map(int, input().split()))
setAbonnement = [set() for _ in range(numberOfPerson)]
setFollower = [set() for _ in range(numberOfPerson)]

while numberOfConnection != 0:
    numberOfConnection -= 1
    personA, personB = list(map(int, input().split()))
    setAbonnement[personA].add(personB)
    setFollower[personB].add(personA)

max = 0;
for k in range(numberOfPerson):
    currentScore = 0
    setFriends = set.intersection(setAbonnement[k], setFollower[k])
    numberFriend = len(setFriends)
    currentScore += numberFriend * 3 + (len(setFollower[k]) - numberFriend) * 2


    setFollowerOfFriend=set()
    for j in setFriends:
        setFollowerOfFriend=setFollowerOfFriend.union(set.difference(setFollower[j], setFollower[k]))

    if numberFriend>0:
        currentScore+=len(setFollowerOfFriend)-1

    if (currentScore > max):
        max = currentScore

print(max)
