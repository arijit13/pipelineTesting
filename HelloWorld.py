from random import randint
for _ in range(10):
    secret_num=randint(0,10)
count=0
while count<3:
    guess=int(input('Guess: '))
    count+=1
    if guess==secret_num:
        print("Hurrah!!! You have guessed correct number")
        break
    else:
        print(f"Wrong!!! You have: {3-count} guess left")
