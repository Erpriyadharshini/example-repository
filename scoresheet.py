if __name__ =='__main__':
 n=int(input())
 arr=map(int,input().split())
 scores=sorted(list(set(arr)))
 runner_up_score=scores[-2]
 print(runner_up_score)
