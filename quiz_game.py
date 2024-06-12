def check_guess(a,b):
    global score
    attempt=0
    while attempt<3:
        if a.lower()==b.lower():
            score+=1
            print("correct answer")
            break
        else:
            score-=1
            if attempt <2:
                a=input("incorrect guess try again")
            attempt+=1
    if attempt==3:
        print("correct answer is :",b)
    return score

score=0

guess1=input("which bear lives at north pole?")
check_guess(guess1,"polar bear")
guess1=input("which is the fastest land animal?")
check_guess(guess1,"cheetah")
guess1=input("which is the largest  animal?")
check_guess(guess1,"blue whale")
print("your score is",score)