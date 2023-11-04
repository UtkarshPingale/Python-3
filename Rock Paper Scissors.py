import random as rn

rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors= '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("What do you want to choose")
print("1 for Rock, 2 for Paper, 3 for Scissors, 4 for Exit")
a=int(input("Choose : "))
print("You Choose")
if a==1:
    print(rock)
    b=rn.randint(1,4)
    if b==1:
        print(f"Computer Choose\n{rock}")
        print("Its Draw!")
    elif b==2:
        print(f"Computer Choose\n{paper}")
        print("You Lost!")
    elif b==3:
        print(f"Computer Choose\n{scissors}")
        print("Its Won!")

elif a==2:
    print(paper)
    c=rn.randint(1,4)
    if c==1:
        print(f"Computer Choose\n{rock}")
        print("Its Won!")
    elif c==2:
        print(f"Computer Choose\n{paper}")
        print("You Draw!")
    elif c==3:
        print(f"Computer Choose\n{scissors}")
        print("Its Lost!")

elif a==3:
    print(scissors)
    d=rn.randint(1,4)
    if d==1:
        print(f"Computer Choose\n{rock}")
        print("Its Lost!")
    elif d==2:
        print(f"Computer Choose\n{paper}")
        print("You Won!")
    elif d==3:
        print(f"Computer Choose\n{scissors}")
        print("Its Draw!")