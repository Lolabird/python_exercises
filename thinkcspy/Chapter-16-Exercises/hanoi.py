def stackTowers(num): 
    A = []
    B = []
    C = []
    rounds = 0

    
    for i in range(num):
        A.insert(0, i+1)
        

    def hanoi(num, start, aux, end):
        nonlocal rounds  
        
        if num == 1:
            end += [start.pop()]
            rounds += 1
            print(rounds, A, B, C)
        else:
            hanoi(num - 1, start, end, aux)
            end += [start.pop()]
            rounds += 1
            print(rounds, A, B, C)
            hanoi(num -1, aux, start, end)
   
    hanoi(num, A, B, C) 

stackTowers(5)
