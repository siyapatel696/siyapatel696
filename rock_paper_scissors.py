import random
import time
class A:
    def one(self):
        print("WELCOME TO ROCK,PAPER,SCISSORS GAME")
        y=''
        s=0
        while y=='':
            time.sleep(1)
            x=input("enter ROCK / PAPER / SCISSORS:")
            x=x.upper()
            if x!='ROCK' and x!='PAPER' and x!='SCISSORS':
                print("invalid input")
                continue
            
            z=random.randint(1,3)
            if z==1:
                c='ROCK'
                print(c,' X ',x) 
                if x=='PAPER':
                    print("you win!")
                    s+=1
                if x=='SCISSORS':
                    print("computer wins!")
            if z==2:
                c='PAPER'
                print(c,' X ',x)
                if x=='SCISSORS':
                    print("you win!")
                    s+=1
                if x=='ROCK':
                    print("computer wins!")
                    
            if z==3:
                c='SCISSORS'
                print(c,' X ',x)
                if x=='ROCK':
                    print("you win!")
                    s+=1
                if x=='PAPER':
                    print("computer wins!")
                
            if c==x:
                print("It's a tie!")
                
            time.sleep(1)
            print('your score:',s)
            time.sleep(1)
            y=input('press "enter" to play again or "stop" to end game ')
            if y=='':
                continue
            if y!='' or'end':
                y=input('press "enter" to play again or "stop" to end game ')
                
                
            
a1=A()
a1.one()
        
