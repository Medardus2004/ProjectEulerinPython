from argparse import ArgumentParser
import json

def read_data(pokertext):
    datei =  open(pokertext, "r")
    poker_game = []
    for zeile in datei :
        poker_game.append(zeile)
    return(poker_game)

#def check_royal_flush(hand) :
#    if check_flush(hand) and 

#def check_straight_flush(hand) :
#    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1] : 

def check_flush(hand) :
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1] :
        return 600
    else :
        return 0

def main():
    parser = ArgumentParser(description= "Task 54")
    parser.add_argument( "path", help="How many hands does Player 1 win?")
    args = parser.parse_args()
    poker_games =  read_data(args.path)

    # poker_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    poker_order = {key: i for i, key in enumerate(['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'])}
    
    for game in range(0, 20 ) : #len(poker_games)) :
        hand_player_1 = [ 
            {'rank':  poker_games[game][0]  , 'color':  poker_games[game][1] }, 
            {'rank':  poker_games[game][3]  , 'color':  poker_games[game][4]} ,
            {'rank':  poker_games[game][6]  , 'color':  poker_games[game][7]} ,
            {'rank':  poker_games[game][9]  , 'color':  poker_games[game][10]} ,
            {'rank':  poker_games[game][12] , 'color':  poker_games[game][13] } 
        ]

        hand_player_2 = [ 
            {'rank':  poker_games[game][15] , 'color':  poker_games[game][16] }, 
            {'rank':  poker_games[game][18] , 'color':  poker_games[game][19]} ,
            {'rank':  poker_games[game][21] , 'color':  poker_games[game][22]} ,
            {'rank':  poker_games[game][24] , 'color':  poker_games[game][25]} ,
            {'rank':  poker_games[game][27] , 'color':  poker_games[game][28] } 
        ]
        
        print(check_flush(sorted(hand_player_1, key=lambda d: poker_order[d['rank']])))

        #order = {key: i for i, key in enumerate(poker_order)}
        #sorted(hand_player1_order, key=lambda d: order[d['value']])


if __name__ == "__main__":
    main() 