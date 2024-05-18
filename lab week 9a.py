# Ruiyang Shi

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

from numpy import random

choices = ['rock', 'paper', 'scissors']

p1 = input('Pick one of rock, paper or scissors: ')
p2 = random.choice(choices)



from numpy import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.winning_conditions = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }
    
    def get_computer_choice(self):
        return random.choice(self.choices)

    def get_human_choice(self, player):
        while True:
            choice = input(f"{player}, pick one of rock, paper or scissors (or quit to exit): ").lower()
            if choice in self.choices or choice == 'quit':
                return choice
            else:
                print("Invalid input. Please try again.")

    def determine_winner(self, choice1, choice2):
        if choice1 == choice2:
            return "tie"
        elif self.winning_conditions[choice1] == choice2:
            return "player1"
        else:
            return "player2"
    
    def play(self):
        print("Welcome to Rock Paper Scissors!")
        print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
        print("If both players choose the same, it's a tie.")
        
        num_players = int(input("Enter number of human players (0-2): "))
        players = [input(f"Enter name for player {i+1}: ") for i in range(num_players)]
        players += [f"Computer {i+1}" for i in range(2-num_players)]

        player_wins = {p: 0 for p in players}

        while True:
            player_choices = []
            for player in players:
                if player.startswith('Computer'):
                    player_choices.append(self.get_computer_choice())
                else:
                    player_choices.append(self.get_human_choice(player))
                    if player_choices[-1] == 'quit':
                        break
            
            if 'quit' in player_choices:
                break
            
            print("Choices:")
            for player, choice in zip(players, player_choices):
                print(f"{player} picked {choice}")

            winner = self.determine_winner(player_choices[0], player_choices[1])
            if winner == "tie":
                print("It's a tie!")
            else:
                winner = players[0] if winner == "player1" else players[1]
                print(f"{winner} wins!")
                player_wins[winner] += 1
            
            print("Current scores:")
            for player, wins in player_wins.items():
                print(f"{player}: {wins}")
            print()
        
        print("Final scores:")
        for player, wins in player_wins.items():
            print(f"{player}: {wins}")
        
        winner = max(player_wins, key=player_wins.get)
        print(f"{winner} is the final winner!")

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play()