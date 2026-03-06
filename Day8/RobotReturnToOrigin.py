lass Solution:
    def judgeCircle(self, moves: str) -> bool:
        sum1=0
        sum2=0
        for i in range (len(moves)):
            if(moves[i]=='U'):
                sum1+=1
            elif(moves[i]=='D'):
                sum1-=1
            elif(moves[i]=='L'):
                sum2+=1
            elif(moves[i]=='R'):
                sum2-=1
        if(sum1==0 and sum2==0):
            return True
        else :
            return False
