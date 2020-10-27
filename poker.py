#Poker Hand Sorter - python language

#Task - Finding the winner in a 2 player poker from a stream of hands
#       This is done by the finding the winner in each hands and summing the total wins of each player
#       In case of a unbreakable tie, a win is given to both players
#
#Assumptions made - 1) The cards are valued in the order: 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace
#                   2) Suits are not taken into account to break a tie for this exercise - only the value of the card determines a winner
#
#Flags for each combination - {Royal Flush -'RF', Straight Flush - 'SF',Four of a kind - 'FK',Full House -'FH',Flush -'FL',
#                              Straight - 'ST', Three of a kind - 'TK', Two Pairs - 'TP',Pair - 'PA', High Card -'HC' }

#Main program - Program starts from here
def main():
    try:
        
        P1_win = 0 
        P2_win = 0

        try:
            #Opens the input file containing the stream of hands in read only mode
            infile = open('input.txt','r')
            final = 0

            #Reading the file contents line by line
            for line in infile:
                card = line

                #Separating Player1 hand and Player2 hand
                P1_card_value = card[0:14:3]
                P1_card_type = card[1:14:3]
                
                P2_card_value = card[15:29:3]
                P2_card_type = card[16:29:3]

                #Determining the combination of each player's hand
                P1_hand,P1_pvalue = determineHand(P1_card_value, P1_card_type)
                P2_hand,P2_pvalue = determineHand(P2_card_value, P2_card_type)

                #Finding the winner of each hand
                final = compare(P1_hand, P2_hand, P1_card_value, P2_card_value, P1_pvalue, P2_pvalue)

                #Assigning the win to corresponding player
                if final == 'P1':
                    P1_win = P1_win + 1
                elif final == 'P2':
                    P2_win = P2_win + 1
                else:
                    P1_win = P1_win + 1
                    P2_win = P2_win + 1

            infile.close()  #Closing the file

        except IOError:
            print("Unable to read input file ","poker-hands.txt")
            

        #Final Output of total wins by each player
        print("Player1: ",P1_win)
        print("Player2: ",P2_win)
        
    except:
        print("An error occurred")

#Determining the combination of player's hand
def determineHand(card_value, card_type):
    pvalue = []
    #Determining if the hand is royal flush
    hand_flag = royal_flush(card_value, card_type)
    
    if hand_flag != 'Y':
        #Determining if the hand is straight flush
        hand_flag = straight_flush(card_value, card_type)
        
        if hand_flag != 'Y':
            #Determining if the hand is four of a kind
            pvalue,hand_flag = fourkind(card_value)
            
            if hand_flag != 'Y':
                #Determining if the hand is full house
                pvalue,hand_flag = fullhouse(card_value)
                
                if hand_flag != 'Y':
                    #Determining if the hand is flush
                    hand_flag = flush(card_type)
                    
                    if hand_flag != 'Y':
                        #Determining if the hand is straight
                        hand_flag = straight(card_value)
                        
                        if hand_flag != 'Y':
                            #Determining if the hand is three of a kind
                            pvalue,hand_flag = threekind(card_value)
                            
                            if hand_flag != 'Y':
                                #Determining if the hand is pairs
                                pvalue,hand_flag = pairs(card_value)
                                
                                if hand_flag == 'N':
                                    hand = 'HC' #High Card Flag set
                                    
                                elif hand_flag == '2P':
                                    hand = 'TP' #Two Pairs Flag set
                                    
                                elif hand_flag == 'P':
                                    hand = 'PA' #Pair Flag set
                            else:        
                                hand = 'TK' #Three of a kind Flag set
                        else:
                             hand = 'ST' #Straight Flag set
                    else:
                        hand = 'FL' #Flush Flag set
                else:
                    hand = 'FH' #Full House Flag set
            else:
                hand = 'FK' #Four of a kind Flag set
        else:
            hand = 'SF' #Straight Flush Flag set
    else:
        hand = 'RF' #Royal Flush Flag set
    return hand,pvalue

#Finding the winner of the hand
def compare(P1_hand, P2_hand, P1_card_value, P2_card_value, P1_pvalue, P2_pvalue):
    
    final = 'P1P2' #Initialize both players flag
    
    if P1_hand != P2_hand: #Player1 and player2 combination are different
        
        #Checking for win combination from highest to lowest
        
        if (P1_hand == 'RF') or (P2_hand == 'RF'): 
            if (P1_hand == 'RF'):
                final = 'P1' #Set Player1 Flag
            else:        
                final = 'P2' #Set Player2 Flag
                
        elif(P1_hand == 'SF') or (P2_hand == 'SF'): 
            if (P1_hand == 'SF'):
                final = 'P1' #Set Player1 Flag
            else:        
                final = 'P2' #Set Player2 Flag
                
        elif(P1_hand == 'FK') or (P2_hand == 'FK'): 
            if (P1_hand == 'FK'):
                final = 'P1' #Set Player1 Flag
            else:        
                final = 'P2' #Set Player2 Flag
                
        elif(P1_hand == 'FH') or (P2_hand == 'FH'): 
            if (P1_hand == 'FH'):
                final = 'P1' #Set Player1 Flag
            else:        
                final = 'P2' #Set Player2 Flag
                
        elif(P1_hand == 'FL') or (P2_hand == 'FL'): 
            if (P1_hand == 'FL'):
                final = 'P1' #Set Player1 Flag
            else:        
                final = 'P2' #Set Player2 Flag
                
        elif(P1_hand == 'ST') or (P2_hand == 'ST'): 
            if (P1_hand == 'ST'):
                final = 'P1' #Set Player1 Flag
            else:        
                final = 'P2' #Set Player2 Flag
                
        elif(P1_hand == 'TK') or (P2_hand == 'TK'):  
            if (P1_hand == 'TK'):
                final = 'P1' #Set Player1 Flag
            else:        
                final = 'P2' #Set Player2 Flag
                
        elif(P1_hand == 'TP') or (P2_hand == 'TP'):
            if (P1_hand == 'TP'):
                final = 'P1' #Set Player1 Flag
            else:        
                final = 'P2' #Set Player2 Flag
                
        elif(P1_hand == 'PA') or (P2_hand == 'PA'):
            if (P1_hand == 'PA'):
                final = 'P1' #Set Player1 Flag
            else:        
                final = 'P2' #Set Player2 Flag
                
    else:
        if (P1_hand == 'HC') and (P2_hand == 'HC'):
            P1_high_value = highCard(P1_card_value)

            P2_high_value = highCard(P2_card_value)

            if(P1_high_value > P2_high_value):
                final = 'P1' #Set Player1 Flag
                
            elif(P2_high_value > P1_high_value):
                final = 'P2' #Set Player2 Flag
                
            else:
                if P1_high_value == P2_high_value:
                
                    P1_high_value = reversesort(P1_card_value)

                    P2_high_value = reversesort(P2_card_value)
                 
                    if(P1_high_value > P2_high_value):
                        final = 'P1' #Set Player1 Flag
                        
                    elif(P2_high_value > P1_high_value):
                        final = 'P2' #Set Player2 Flag
                        
                    else:
                        print("HC-Both hands are identical")
                        
        elif (P1_hand == 'TP') and (P2_hand == 'TP'):
            
                if(P1_pvalue[0] > P2_pvalue[0]):
                    final = 'P1' #Set Player1 Flag
                    
                elif(P2_pvalue[0] > P1_pvalue[0]):
                    final = 'P2' #Set Player2 Flag
                    
                elif(P1_pvalue[1] > P2_pvalue[1]):
                    final = 'P1' #Set Player1 Flag
                    
                elif(P2_pvalue[1] > P1_pvalue[1]):
                    final = 'P2' #Set Player2 Flag
                    
                else:
                    P1_high_value = reversesort(P1_card_value)

                    P2_high_value = reversesort(P2_card_value)
                    
                    if(P1_high_value > P2_high_value):
                        final = 'P1' #Set Player1 Flag
                        
                    elif(P2_high_value > P1_high_value):
                        final = 'P2' #Set Player2 Flag
                        
                    else:
                        print("TP-Both hands are identical")
            
        elif (P1_hand == 'PA') and (P2_hand == 'PA'):

            if(P1_pvalue > P2_pvalue):
                final = 'P1' #Set Player1 Flag
                
            elif(P2_pvalue > P1_pvalue):
                final = 'P2' #Set Player2 Flag
                
            else:
                P1_high_value = reversesort(P1_card_value)

                P2_high_value = reversesort(P2_card_value)
             
                if(P1_high_value > P2_high_value):
                    final = 'P1' #Set Player1 Flag
                    
                elif(P2_high_value > P1_high_value):
                    final = 'P2' #Set Player2 Flag
                    
                else:
                    print("PA-Both hands are identical")
                    
        elif (P1_hand == 'TK') and (P2_hand == 'TK'):

            if(P1_pvalue > P2_pvalue):
                final = 'P1' #Set Player1 Flag
                
            elif(P2_pvalue > P1_pvalue):
                final = 'P2' #Set Player2 Flag
                
            else:
                P1_high_value = reversesort(P1_card_value)

                P2_high_value = reversesort(P2_card_value)
             
                if(P1_high_value > P2_high_value):
                    final = 'P1' #Set Player1 Flag
                    
                elif(P2_high_value > P1_high_value):
                    final = 'P2' #Set Player2 Flag
                    
                else:
                    print("TK-Both hands are identical")
                    
        elif (P1_hand == 'FK') and (P2_hand == 'FK'):

            if(P1_pvalue > P2_pvalue):
                final = 'P1' #Set Player1 Flag
                
            elif(P2_pvalue > P1_pvalue):
                final = 'P2' #Set Player2 Flag
                
            else:
                P1_high_value = reversesort(P1_card_value)

                P2_high_value = reversesort(P2_card_value)
             
                if(P1_high_value > P2_high_value):
                    final = 'P1' #Set Player1 Flag
                    
                elif(P2_high_value > P1_high_value):
                    final = 'P2' #Set Player2 Flag
                    
                else:
                    print("FK-Both hands are identical")

        elif (P1_hand == 'ST') and (P2_hand == 'ST'):

            P1_high_value = reversesort(P1_card_value)

            P2_high_value = reversesort(P2_card_value)
         
            if(P1_high_value > P2_high_value):
                final = 'P1' #Set Player1 Flag
                
            elif(P2_high_value > P1_high_value):
                final = 'P2' #Set Player2 Flag
                
            else:
                print("ST-Both hands are identical")

        elif (P1_hand == 'FL') and (P2_hand == 'FL'):

            P1_high_value = reversesort(P1_card_value)

            P2_high_value = reversesort(P2_card_value)
         
            if(P1_high_value > P2_high_value):
                final = 'P1' #Set Player1 Flag
                
            elif(P2_high_value > P1_high_value):
                final = 'P2' #Set Player2 Flag
                
            else:
                print("FL-Both hands are identical")
                
        elif (P1_hand == 'SF') and (P2_hand == 'SF'):

            P1_high_value = reversesort(P1_card_value)

            P2_high_value = reversesort(P2_card_value)
         
            if(P1_high_value > P2_high_value):
                final = 'P1' #Set Player1 Flag
                
            elif(P2_high_value > P1_high_value):
                final = 'P2' #Set Player2 Flag
                
            else:
                print("SF-Both hands are identical")

        elif (P1_hand == 'FH') and (P2_hand == 'FH'):

            if(P1_pvalue[0] > P2_pvalue[0]):
                final = 'P1' #Set Player1 Flag
                
            elif(P2_pvalue[0] > P1_pvalue[0]):
                final = 'P2' #Set Player2 Flag
                
            elif(P1_pvalue[1] > P2_pvalue[1]):
                final = 'P1' #Set Player1 Flag
                
            elif(P2_pvalue[1] > P1_pvalue[1]):
                final = 'P2' #Set Player2 Flag
                
            else:
                print("FH-Both hands are identical")

        else:
            print("Identical")
    return final

#Sort the card values in descending order
def reversesort(card_value):
    card_value = conversion(card_value)
    card_value.sort(reverse=True)
    return card_value

#Converting all the card values to integer
def conversion(card_value):
    value = ['2','3','4','5','6','7','8','9']
    con_value = [0,0,0,0,0]
    length = len(card_value)
    for i in range(0,length):
        if card_value[i] not in value:
            if card_value[i] == 'T':
                con_value[i] = 10
            elif card_value[i] == 'J':
                con_value[i] = 11                                
            elif card_value[i] == 'Q':
                con_value[i] += 12
            elif card_value[i] == 'K':
                con_value[i] += 13
            elif card_value[i] == 'A':
                con_value[i] += 14
        else:
            con_value[i] += int(card_value[i])
    
    return con_value

#Determining if the hand is royal flush       
def royal_flush(card_value, card_type):
    royal_card = ['T','J','Q','K','A']
    check = []
    royal = 0
    flag = 'N'
    if card_type[0] == card_type[1]:
        if card_type[1] == card_type[2]:
            if card_type[2] == card_type[3]:
                if card_type[3] == card_type[4]:
                    for i in range(0,5):
                        if card_value[i] in royal_card:
                            royal = royal + 1
                            if card_value[i] not in check:
                                check += card_value[i]
                            else:
                                break
    if royal == 5:
        flag = 'Y'
    return flag
                                
#Determining if the hand is straight flush                                
def straight_flush(card_value, card_type):
    con_value = conversion(card_value)
    flag = 'N'
    if card_type[0] == card_type[1]:
        if card_type[1] == card_type[2]:
            if card_type[2] == card_type[3]:
                if card_type[3] == card_type[4]:
                    con_value.sort()
                    temp = con_value[4]
                    if temp == con_value[3] + 1:
                        if temp == con_value[2] + 2:
                            if temp == con_value[1] + 3:
                                if temp == con_value[0] + 4:
                                    flag = 'Y'
    return flag

#Determining if the hand has 1 or 2 pairs
def pairs(card_value):
    con_value = conversion(card_value)
    pair = 'N'
    temp_value = con_value
    count = 0
    x = []
    for i in range(0,4):
        k = i + 1
        for j in range(k,5):
            if temp_value[i] == temp_value[j]:
                if temp_value[i] not in x:
                    x.append(temp_value[i])
                count = count + 1 

    if count > 0:
        if count == 1:
            x[0] = int(x[0])
            pair = 'P'
        elif count == 2:
            for i in range(0,2):
                x[i] = int(x[i])
            x.sort(reverse=True)
            pair = '2P'
    return x,pair
        
#Determining if the hand is straight
def straight(card_value):
    con_value = conversion(card_value)
    con_value.sort()
    flag = 'N'
    temp = con_value[4]
    if temp == con_value[3] + 1:
        if temp == con_value[2] + 2:
            if temp == con_value[1] + 3:
                if temp == con_value[0] + 4:
                    flag = 'Y'
    return flag

#Determining if the hand is three of a kind
def threekind(card_value):
    con_value = conversion(card_value)
    x = 0
    y = []
    flag = 'N'
    for i in range(0,5):
        x = con_value.count(con_value[i])
        if x == 3:
            if con_value[i] not in y:
                y.append(con_value[i])
            flag = 'Y'
    return y,flag

#Determining if the hand is four of a kind
def fourkind(card_value):
    con_value = conversion(card_value)
    x = 0
    y = []
    flag = 'N'
    for i in range(0,2):
        x = con_value.count(con_value[i])
        if x == 4:
            if con_value[i] not in y:
                y.append(con_value[i])
            flag = 'Y'
    return y,flag

#Determining if the hand is full house
def fullhouse(card_value):
    con_value = conversion(card_value)
    x = 0
    y = []
    flag = 'N'
    p = 'N'
    three = 'N'
    for i in range(0,5):
        x = con_value.count(con_value[i])
        if x == 2:
            if con_value[i] not in y:
                y.append(con_value[i])
            p = 'Y'

        if x == 3:
            if con_value[i] not in y:
                y.append(con_value[i])
            three = 'Y'

    if p == 'Y' and three == 'Y':
        flag = 'Y'
    return y,flag
        
#Determining if the hand is flush
def flush(card_type):
    flag = 'N'
    if card_type[0] == card_type[1]:
        if card_type[1] == card_type[2]:
            if card_type[2] == card_type[3]:
                if card_type[3] == card_type[4]:
                    flag = 'Y'
    return flag

#Determining if the hand is High Card
def highCard(card_value):
    con_value = conversion(card_value)
    high_card = con_value[0]

    for i in range(1,5):
        if con_value[i] > high_card:
            high_card = con_value[i]         
    return high_card     
          
main() #Main program call
