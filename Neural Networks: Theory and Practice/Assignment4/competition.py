from c4 import Board
from c4 import AgentRandom, AgentMinMaxMC, AgentMC, MyAgent
from models import *

def game(agent_a, agent_b):
    b = Board()
    agents = [agent_a, agent_b]
    moves = []
    
    who = 0
    
    while not b.end():
        m = agents[who].best_move(b)
        b.apply_move(m) 
        who = 1-who
    
    b.print() 
    print (b.result)
    print('last move: ', b.last_moves)
    
    return b.result
    
def duel(agent_a, agent_b, N):
    score = {1:0, -1:0, 0:0}
    
    for i in range(N):
        r1 = game(agent_a, agent_b)
        score[r1] += 1
        r2 = game(agent_b, agent_a)
        score[-r2] += 1
    
    s = sum(score.values())
    
    for k in score:
        score[k] /= s    
    print (f'{agent_a.name}: {score[+1]}, {agent_b.name}: {score[-1]}, Draw: {score[0]}')     
    
    
if __name__ == '__main__': 
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # A = MyAgent(CNN1, 'CNN1_new.pth', device) # 65%
    # A = MyAgent(CNN_1_channel, 'CNN_1_channel.pth', device) # 58%
    # A = MyAgent(CNN_3_channel, 'CNN_3_channel.pth', device) # 62% / 75% z ifem
    A = MyAgent(CNN1, 'CNN1.pth', device) # 65%
    # A = MyAgent(CNN2, 'CNN2.pth', device) # 35%
    # A = MyAgent(CNN3, 'CNN3.pth', device) # 40%
    # A = MyAgent(CNN2, 'CNN2_stare.pth', device) # nie dziala
    # A = MyAgent(NN1, 'NN1.pth', device) # 72%
    B = AgentRandom()
    # B = AgentMC(50)    
    # B = AgentMC(10)
    # B = AgentMinMaxMC(3,10)
    
    duel(A, B, 1000)    