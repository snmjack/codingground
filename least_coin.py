import numpy as np
from itertools import permutations
x, y = [int(x) for x in raw_input().split()]  
w=[]
for i in range(0,x):
   w.append(int(raw_input(),2))
w_bin = []
for i in range(0,x):
    w_bin.append(format(w[i],'b').zfill(y))
print w_bin
def countSetBits(num):
     binary = bin(num)
     setBits = [ones for ones in binary[2:].zfill(y) if ones=='1']
     return len(setBits)
one_count = []
for i in range(0,x):
    one_count.append(countSetBits(w[i]))
perm_num = []
for i in range(0,x):
    perm_num.append(i)
perm = permutations(perm_num)
perm_list = []
for i in list(perm):
    perm_list.append(i)
print perm_list
coin_list = []
for i in perm_list:
    global_weapon = []
    global_count_list = []
    
    print 'In List -------------------------------', i
    for a in range(0,y):
        global_weapon.insert(a,0)
    for j in i:
        weapon = w_bin[j]
        print '\n'
        print 'Weapon ---------------- ', weapon
        local_weapon = []
        for i in range(0,y):
            local_weapon.insert(i,0)
        #print 'Local Weapon - ZERO',  local_weapon
        for p in range(0,y):
            #print 'Loop P', p
            if weapon[p] == '1':
                #print 'Weapon for P', weapon[p]
                #local_weapon[p]=weapon[p]
                local_weapon[p]=1
            #print 'Local Weapon - updated', local_weapon
        flag = 0
        flag2 = 0
        count = 0
        #local_count = []
        for i in range(0,y):
            global_count = []
            if global_weapon[i]==0:
                global_weapon[i] = local_weapon[i]
                
            local_count = sum(global_weapon)
            print 'Global Weapon - updated', global_weapon
            print 'Local Count - updated', local_count
            
            if flag == 0:
                print 'Flag ---- 0_0 ---'
                global_count.append(local_count)
                print 'Global Count first', global_count
                flag = 1
            elif flag == 1:
                print 'Flag ---- 0_1 ---'
                diff =  local_count - sum(global_count)
                if diff < 0 or sum(global_count) > y:
                    break
                else:
                    global_count.append(diff)
                    print 'Global Count diff',global_count
                
                
                
            '''    
                if diff < 0:
                    break
                elif diff >= 0:
                    global_count.append(diff)
                    print 'Global Count diff',global_count
            
            
            if flag2 == 0:
                print 'Flag ---- 1_0 ---'
                global_count_list.append(global_count)
                print 'Global Count list first', global_count_list
                flag2 = 1
            elif flag2 == 1:
                print 'Flag ---- 1_1 ---'
                diff2 =  sum(global_count_list) - sum(global_count)
                if sum(global_count_list) > y:
                    break
                else:
                    global_count_list.append(diff)
                    print 'Global Count list diff',global_count_list
            
            '''
        #count = abs(count - local_count)
        #global_count.append(count)
        print 'Global Count =====', global_count
        
        if sum(global_count_list) < sum(global_count):
            print ' Check Global count list', global_count_list
            print ' Check Global count', global_count
            diff3 = sum(global_count) - sum(global_count_list)
            print ' Check diff3 ', diff3
            global_count_list.append(diff3)
                
        print 'Global Count List =====', global_count_list
        coins = 0
        for i in range(0,len(global_count_list)):
            coins = coins + (global_count_list[i]**2)
        print ' Coins === ', coins
    
    coin_list.append(coins)
    print ' Coins List ', coin_list     
    
least_coin = min(x for x in coin_list)
print least_coin
