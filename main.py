import random
'''
    Rules:
        All the players get a chance to score above 50
        if any player reach 50 they got the highest score until the ends last player is remaining
        if the last player scored more than any player then he/she wins
'''
def roll():
    max_val = 6
    min_val = 1
    roll = random.randint(min_val,max_val)

    return roll

while True:
    players = input("Enter number of players (1-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <=4:
            break
        else:
            print("Must be between 2-4 players")
    else:
        print("Invalid Try again")


max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score) < max_score:
    for player_idx in range(players):
        print("\nPlayer number",player_idx + 1,"turn has just started!")
        print("Your total score is: ",player_score[player_idx],"\n")
        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if(should_roll.lower() != "y"):
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:",value)

            print("Your score is: ",current_score)

            player_score[player_idx] += current_score
            print("Your total score is:",player_score[player_idx])

max_score = max(player_score)
win = player_score.index(max_score)
print("player number",win+1,"is the winner with a score of:",max_score)

