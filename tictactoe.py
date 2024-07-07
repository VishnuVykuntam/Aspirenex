import math

def printstate(position):
    print(f' {position[0]} | {position[1]} | {position[2]}\n-----------\n {position[3]} | {position[4]} | {position[5]}\n-----------\n {position[6]} | {position[7]} | {position[8]}\n\n')
      
k=10

def minimax(state, player):
    # printstate(state)
    global k
    global alpha
    global beta
    # print(' i am k ',k)
    number=state.count(' ')
    x=game_over(state)
    if x:
        # print('X win' if x==1 else 'O win')
        return x
    elif number == 0:
        # print('draw')
        return 0
    else:
        if player:
            maxeval=-math.inf
            for i in range(9):
                if state[i] == ' ':
                    state[i]='X'
                    eval=minimax(state,False)
                    state[i]=' '
                    # print(eval,'\n')
                    eval=eval*(number+1)
                    # print(eval,'\n')
                    if maxeval<=eval:
                        maxeval=eval
                        k=i
                    # maxeval=max(eval,maxeval)
                    # alpha=max(alpha,eval)
                    # if beta<=alpha:
                    #     break
            return maxeval
        else:
            mineval=math.inf
            for i in range(9):
                if state[i]==' ':
                    state[i]='O'
                    eval=minimax(state,True)
                    state[i]=' '
                    # print(eval,'\n')
                    eval=eval*(number+1)
                    # print(eval,'\n')
                    # mineval=min(eval,mineval)
                    if mineval>=eval:
                        mineval=eval
                        k=i
                    # beta=min(beta,eval)
                    # if beta<=alpha:
                    #     break
            return mineval

def best_play(state):
    best=-math.inf
    best_move=None
    for i in range(9):
        if state[i]==' ':
            state[i]="X"
            move_eval=minimax(state,False)
            state[i]=" "
            if move_eval>best:
                best=move_eval
                best_move=i
    print(f'best move {best_move} k {k}')
    return best_move


def game_over(state):

    if(state[0]==state[1]==state[2]=='X'):
        return 1
    elif(state[3]==state[4]==state[5]=='X'):
        return 1
    elif(state[6]==state[7]==state[8]=='X'):
        return 1
    elif(state[6]==state[3]==state[0]=='X'):
        return 1
    elif(state[1]==state[4]==state[7]=='X'):
        return 1
    elif(state[2]==state[5]==state[8]=='X'):
        return 1
    elif(state[0]==state[4]==state[8]=='X'):
        return 1
    elif(state[2]==state[4]==state[6]=='X'):
        return 1
    elif(state[3]==state[4]==state[5]=='O'):
        return -1
    elif(state[0]==state[1]==state[2]=='O'):
        return -1
    elif(state[8]==state[7]==state[6]=='O'):
        return -1
    elif(state[0]==state[3]==state[6]=='O'):
        return -1
    elif(state[1]==state[4]==state[7]=='O'):
        return -1
    elif(state[2]==state[5]==state[8]=='O'):
        return -1
    elif(state[0]==state[4]==state[8]=='O'):
        return -1
    elif(state[2]==state[4]==state[6]=='O'):
        return -1
    else:
        return 0
    

def result(score):
    if score>0:
        print('X wins')
    elif score <0:
        print('O wins')
    else:
        print('draw')



position=[' ' for i in range(9)]
position[0]=' '
position[1]=' '
position[2]=' '
position[3]=' '
position[4]=' '
position[5]=' '
position[6]=' '
position[7]=' '
position[8]=' '
# printstate(position)

alpha=-math.inf
beta=math.inf

# score=minimax(position,alpha,beta,1)
# result(score)

def user_play():
    print("enter the location to put your piece")
    x=int(input())
    position[x]='O'
    printstate(position)



def ai_play():
    move=best_play(position)
    global k
    position[move]='X'
    printstate(position)


printstate(position)
while not game_over(position):
    
    # print('game not over')
    if not game_over(position):
        # print(' ai to play')
        if position.count(' ') !=0:
            # print(' ai can play')
            ai_play()
        else:
            break
    if  not game_over(position):
        if position.count(' ') !=0:
            print(f'{position.count(' ')} remaining places to play')
            user_play()
    else:
        break
    

who=game_over(position)
result(who)

# user_play()
# ai_play()
    
# print(k)
















