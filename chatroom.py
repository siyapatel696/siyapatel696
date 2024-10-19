from datetime import datetime
import time
class A:
    def one(self):
        print('CHAT ROOM-1 :')
        self.a=input("A: type a message:")
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.b=input("B: type a message:")
        self.timestamp2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class B(A):
    def two(self):
        time.sleep(1)
        print("CHAT ROOM-1 HISTORY:")
        print("A:",self.a,self.timestamp)
        time.sleep(1)
        print("B:",self.b,self.timestamp2)
b1=B()
b1.one()
b1.two()
class C:
    def three(self):
        print('CHAT ROOM-1 :') self.c=input("A: type a message:")
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.d=input("B: type a message:") self.timestamp2 =
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class D(C):
    def four(self):
        time.sleep(1)
        print("A:",self.c,self.timestamp)
        time.sleep(1)
        print("B:",self.d,self.timestamp2)
d1=D()
d1.three()
b1.two()
d1.four()

    


        
        
        
        
        
        
        
