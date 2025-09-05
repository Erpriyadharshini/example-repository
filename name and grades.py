if __name__ == '__main__':
    for _ in range (int(input())):
     name=input()
     score=float(input())
     if _ == 0:
        scoresheet =[[name,score]]
     else:
        scoresheet.append([name,score])
        scoresheet.sort(key=lambda x: x[1])
        if scoresheet[-1][1] == scoresheet[-2][1]:
            scoresheet.pop()
        elif scoresheet[-1][1] == scoresheet[-3][1]:
           scoresheet.pop()
           scoresheet.pop()
        else:
              scoresheet.pop()
              scoresheet.pop()
              scoresheet.pop()
              scoresheet.sort()
              for i in scoresheet:
                 print(i[0])
                 break
                 
        