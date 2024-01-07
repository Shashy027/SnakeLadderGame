import random

class SnakeGame:
    def __init__(self, grid_size, num_players):
        # Initialize the game with grid size and number of players
        self.grid_size = grid_size
        self.num_players = num_players
        self.players = {f"Player {i+1}": 0 for i in range(num_players)}
        self.winner = None
        self.player_positions = {f"Player {i+1}": [] for i in range(num_players)} # Record player positions

    def roll_dice(self):
        # Roll a dice, returning a number between 1 and 6
        return random.randint(1, 6)

    def move_player(self, player):
        # Player rolls the dice
        total_roll = 0
        roll = self.roll_dice()
        total_roll += roll

        # Check if the player rolls a 6 and give an extra roll
        if roll == 6:
            print(f"{player} rolled a 6 and gets an extra roll!")
            extra_roll = self.roll_dice()
            total_roll += extra_roll
            print(f"{player} rolled an extra {extra_roll} on the second roll.")

        potential_position = self.players[player] + total_roll

        # Check if the potential position exceeds the grid size
        if potential_position <= self.grid_size ** 2:
            # Check if another player is already in this position
            if any(self.players[other_player] == potential_position for other_player in self.players if other_player != player):
                print(f"{player} landed on a position occupied by another player and must start over!")
                self.players[player] = 0
            else:
                self.players[player] = potential_position
        else:
            # Player cannot move beyond the grid size
            print(f"{player} cannot move beyond position {self.grid_size ** 2}.")

        self.player_positions[player].append(self.players[player])  # Record position after the move
        print(f"{player} moved to position {self.players[player]}")

    def check_winner(self, player):
        # Check if the player has reached the final position
        if self.players[player] == self.grid_size ** 2:
            self.winner = player
            return True
        return False

    def play_game(self):
        # Main game loop
        while not self.winner:
            for player in self.players:
                self.move_player(player)
                if self.check_winner(player):
                    print(f"{player} wins!")
                    return
                input("Press Enter to continue to the next player...")

    def show_final_results(self):
        # Show the final positions of each player
        print("\nGame Over! Final Results:")
        for player, positions in self.player_positions.items():
            print(f"{player} positions: {positions}")

# Set up and start the game
grid_size = int(input("Enter grid size (e.g., 1 for a 1x1 grid): "))
num_players = 2

game = SnakeGame(grid_size, num_players)
game.play_game()
game.show_final_results()

