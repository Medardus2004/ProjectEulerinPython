from argparse import ArgumentParser
import numpy as np

def read_data(pokertext):
    datei =  open(pokertext, "r")
    poker_game = []
    for zeile in datei :
        poker_game.append(zeile)
    return(poker_game)

def number_converter(letter) :
    if letter == 'T':
        return 10
    if letter == 'J' :
        return 11
    if letter == 'Q' :
        return 12
    if letter == 'K' :
        return 13
    if letter == 'A' :
        return 14
    return letter

def check_royal_flush(hand) :
    if check_straight_flush(hand) and  hand[0]["rank"] == 'T' :
        return True
    else : 
        return False

def check_straight_flush(hand) :
    if check_straight([number_converter(hand[0]["rank"]), number_converter(hand[1]["rank"]), number_converter(hand[2]["rank"]), number_converter(hand[3]["rank"]), number_converter(hand[4]["rank"])]) and check_flush([hand[0]["color"], hand[1]["color"], hand[2]["color"], hand[3]["color"], hand[4]["color"]]) : 
        return True
    else :
        return False
    
def check_four_of_a_kind(hand_rank) :
    if any(hand_rank.count(i)==4 for i in set(hand_rank)) :
        return True
    else :
        return False
    
def check_full_house(hand_rank) :
    if any(hand_rank.count(i)==3 for i in set(hand_rank)) and any(hand_rank.count(i)==2 for i in set(hand_rank)):
        return True
    else :
        return False

def check_flush(hand_color) :
    if hand_color[0] == hand_color[1] == hand_color[2] == hand_color[3] == hand_color[4] :
        return True
    else :
        return False

def check_flush(hand_color) :
    if hand_color[0] == hand_color[1] == hand_color[2] == hand_color[3] == hand_color[4] :
        return True
    else :
        return False

def check_straight(hand_rank) :
    if int(hand_rank[1]) - int(hand_rank[0]) == 1 and int(hand_rank[2]) - int(hand_rank[1]) == 1 and int(hand_rank[3]) - int(hand_rank[2]) == 1 and int(hand_rank[4]) - int(hand_rank[3]) == 1 : 
        return True
    else :
        return False

def check_three_of_a_kind(hand_rank) :
    if any(hand_rank.count(i)==3 for i in set(hand_rank)) :
        return True
    else :
        return False

def check_two_pairs(hand_rank) :
    if any(hand_rank.count(i)==2 for i in set(hand_rank)) and len(set(hand_rank)) == 3:
        return True
    else :
        return False

def check_one_pair(hand_rank) :
    if any(hand_rank.count(i)==2 for i in set(hand_rank)) :
        hand_rank_copy = hand_rank
        r = (list(set(hand_rank)))
        hand_rank_copy.remove(r[0])
        hand_rank_copy.remove(r[1])
        hand_rank_copy.remove(r[2])
        hand_rank_copy.remove(r[3])
        r.remove(hand_rank_copy[0])
        for i in range(0, len(r)):
            r[i] = int(number_converter(r[i]))
        sorted(r)
        return 1000000 + highest_card(int(number_converter(hand_rank_copy[0])), r[0], r[1])
    else :
        return 0


def highest_card(hand1, hand2, hand3) :
    return hand1 * 10000 + hand2 * 100 + hand3

def main():
    parser = ArgumentParser(description= "Task 54")
    parser.add_argument( "path", help="How many hands does Player 1 win?")
    args = parser.parse_args()
    poker_games =  read_data(args.path)

    # poker_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    poker_order = {key: i for i, key in enumerate(['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'])}
    
    for game in range(0, 20 ) : #len(poker_games)) :
        score_player_1 = 0
        score_player_2 = 0
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
        hand_rank_player1_sorted = sorted(hand_player_1, key=lambda d: poker_order[d['rank']])
        hand_rank_player2_sorted = sorted(hand_player_2, key=lambda d: poker_order[d['rank']])


        ### Check Royal Flush
        if check_royal_flush(hand_rank_player1_sorted) :
            print("0")
        #if check_royal_flush(hand_rank_player2_sorted) :
        #    print(hand_rank_player2_sorted)

        ### Check Straigh Flush
        elif check_straight_flush(hand_rank_player1_sorted) :
            print("0")
        #if check_straight_flush(hand_rank_player2_sorted) :
        #    print(hand_rank_player2_sorted)

        ### Check Four_of_a_kind
        elif check_four_of_a_kind([number_converter(hand_rank_player1_sorted[0]["rank"]), number_converter(hand_rank_player1_sorted[1]["rank"]), number_converter(hand_rank_player1_sorted[2]["rank"]), number_converter(hand_rank_player1_sorted[3]["rank"]), number_converter(hand_rank_player1_sorted[4]["rank"])]) :
            print("0")
        #if check_four_of_a_kind([number_converter(hand_rank_player2_sorted[0]["rank"]), number_converter(hand_rank_player2_sorted[1]["rank"]), number_converter(hand_rank_player2_sorted[2]["rank"]), number_converter(hand_rank_player2_sorted[3]["rank"]), number_converter(hand_rank_player2_sorted[4]["rank"])]) :
        #    print(hand_rank_player2_sorted)

        ### check Full_house
        elif check_full_house([number_converter(hand_rank_player1_sorted[0]["rank"]), number_converter(hand_rank_player1_sorted[1]["rank"]), number_converter(hand_rank_player1_sorted[2]["rank"]), number_converter(hand_rank_player1_sorted[3]["rank"]), number_converter(hand_rank_player1_sorted[4]["rank"])]) :
            print("0")
        #if check_full_house([number_converter(hand_rank_player2_sorted[0]["rank"]), number_converter(hand_rank_player2_sorted[1]["rank"]), number_converter(hand_rank_player2_sorted[2]["rank"]), number_converter(hand_rank_player2_sorted[3]["rank"]), number_converter(hand_rank_player2_sorted[4]["rank"])]) :
        #    print(hand_rank_player2_sorted)

        ### check Flush
        elif check_flush([hand_player_1[0]["color"], hand_player_1[1]["color"], hand_player_1[2]["color"], hand_player_1[3]["color"], hand_player_1[4]["color"]]) :
            score_player_1 = 600
        #if check_flush([hand_player_2[0]["color"], hand_player_2[1]["color"], hand_player_2[2]["color"], hand_player_2[3]["color"], hand_player_2[4]["color"]]) :
        #    score_player_2 = 600

        ### check Straight
        elif check_straight([number_converter(hand_rank_player1_sorted[0]["rank"]), number_converter(hand_rank_player1_sorted[1]["rank"]), number_converter(hand_rank_player1_sorted[2]["rank"]), number_converter(hand_rank_player1_sorted[3]["rank"]), number_converter(hand_rank_player1_sorted[4]["rank"])]) :
            print(hand_rank_player1_sorted)
        #if check_straight([number_converter(hand_rank_player2_sorted[0]["rank"]), number_converter(hand_rank_player2_sorted[1]["rank"]), number_converter(hand_rank_player2_sorted[2]["rank"]), number_converter(hand_rank_player2_sorted[3]["rank"]), number_converter(hand_rank_player2_sorted[4]["rank"])]) :
        #    print(hand_rank_player2_sorted)

        ### Check Three_of_a_kind
        elif check_three_of_a_kind([number_converter(hand_rank_player1_sorted[0]["rank"]), number_converter(hand_rank_player1_sorted[1]["rank"]), number_converter(hand_rank_player1_sorted[2]["rank"]), number_converter(hand_rank_player1_sorted[3]["rank"]), number_converter(hand_rank_player1_sorted[4]["rank"])]) :
            print(hand_rank_player1_sorted)
        #if check_three_of_a_kind([number_converter(hand_rank_player2_sorted[0]["rank"]), number_converter(hand_rank_player2_sorted[1]["rank"]), number_converter(hand_rank_player2_sorted[2]["rank"]), number_converter(hand_rank_player2_sorted[3]["rank"]), number_converter(hand_rank_player2_sorted[4]["rank"])]) :
        #    print(hand_rank_player2_sorted)

        ### Check two_pairs
        elif check_two_pairs([number_converter(hand_rank_player1_sorted[0]["rank"]), number_converter(hand_rank_player1_sorted[1]["rank"]), number_converter(hand_rank_player1_sorted[2]["rank"]), number_converter(hand_rank_player1_sorted[3]["rank"]), number_converter(hand_rank_player1_sorted[4]["rank"])]) :
            print(hand_rank_player1_sorted)
        #if check_two_pairs([number_converter(hand_rank_player2_sorted[0]["rank"]), number_converter(hand_rank_player2_sorted[1]["rank"]), number_converter(hand_rank_player2_sorted[2]["rank"]), number_converter(hand_rank_player2_sorted[3]["rank"]), number_converter(hand_rank_player2_sorted[4]["rank"])]) :
        #    print(hand_rank_player2_sorted)

        ### Check one_pair
        elif check_one_pair([number_converter(hand_rank_player1_sorted[0]["rank"]), number_converter(hand_rank_player1_sorted[1]["rank"]), number_converter(hand_rank_player1_sorted[2]["rank"]), number_converter(hand_rank_player1_sorted[3]["rank"]), number_converter(hand_rank_player1_sorted[4]["rank"])]) :
            print(hand_rank_player1_sorted, check_one_pair([number_converter(hand_rank_player1_sorted[0]["rank"]), number_converter(hand_rank_player1_sorted[1]["rank"]), number_converter(hand_rank_player1_sorted[2]["rank"]), number_converter(hand_rank_player1_sorted[3]["rank"]), number_converter(hand_rank_player1_sorted[4]["rank"])]))
        #if check_one_pair([number_converter(hand_rank_player2_sorted[0]["rank"]), number_converter(hand_rank_player2_sorted[1]["rank"]), number_converter(hand_rank_player2_sorted[2]["rank"]), number_converter(hand_rank_player2_sorted[3]["rank"]), number_converter(hand_rank_player2_sorted[4]["rank"])]) :
            print(hand_rank_player2_sorted)


        #print(hand_rank_player1_sorted[0]["rank"], hand_rank_player1_sorted[1]["rank"], hand_rank_player1_sorted[2]["rank"], hand_rank_player1_sorted[3]["rank"], hand_rank_player1_sorted[4]["rank"])
        #print(number_converter(hand_rank_player1_sorted[0]["rank"]), number_converter(hand_rank_player1_sorted[1]["rank"]), number_converter(hand_rank_player1_sorted[2]["rank"]), number_converter(hand_rank_player1_sorted[3]["rank"]), number_converter(hand_rank_player1_sorted[4]["rank"]))

if __name__ == "__main__":
    main() 