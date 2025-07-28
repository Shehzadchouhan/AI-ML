import random
def game():
  print("You are playing game...")
  score=random.randint(1,100)

#   fetching highscore
  with open("hiscore.txt") as f:
    hiscore=f.read()
    if(hiscore!=""):
      hiscore=int(hiscore)
    else:
      hiscore=0

  print(f"your score :{score}")
  if(score>hiscore):
    with open("hiscore.txt","w") as f:
      f.write(str(score))

  return score

game()