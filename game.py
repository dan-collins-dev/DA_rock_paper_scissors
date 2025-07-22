from random import randrange

class Game:
    def __init__(self):
        self.score_tracker: dict[str, int] = {"player": 0, "opponent": 0, "ties": 0}
        self.is_running: bool = False
        self.choices: list[str] = ["rock", "paper", "scissors"]
        self.quit_options: list[str] = ["yes", "y", "no", "n"]
    
    
    def start_game(self) -> None:
        self.display_welcome_msg()
        self.is_running = not self.is_running
        self.run_game_loop()
    
    
    def run_game_loop(self) -> None:
        while self.is_running:
            player_choice = self.get_user_choice()
            opponent_choice = self.get_opponent_choice()
            self.compare_choices(player_choice, opponent_choice)
            self.display_scores()
            self.play_again_prompt()
        

    def display_scores(self) -> None:
        print(f"Player Score: {self.score_tracker["player"]} || Opponent's Score: {self.score_tracker["opponent"]} || Ties: {self.score_tracker["ties"]}")


    def add_opponent_point(self) -> None:
        self.score_tracker["opponent"] += 1


    def add_player_point(self) -> None:
        self.score_tracker["player"] += 1

        
    def add_tie(self) -> None:
        self.score_tracker["ties"] += 1

    
    def get_user_choice(self) -> str:
        player_choice = input("\nEnter rock, paper, or scissors: ").lower()
        if player_choice in self.choices:
            return player_choice
        else:
            print("Invalid Option. Try again")
            return self.get_user_choice()

    
    def get_opponent_choice(self) -> str:
        generated_choice_idx = randrange(0, len(self.choices))
        return self.choices[generated_choice_idx]

    
    def display_welcome_msg(self) -> None:
        print("=" * 25)
        print("| Rock, Paper, Scissors |")
        print("=" * 25)
        print("\nWelcome to Rock, Paper, Scissors!\n")

    
    def compare_choices(self, player_choice: str, opponent_choice: str) -> None:
        print(f"\nYour Choice: {player_choice}")
        print(f"Your opponent's choice: {opponent_choice}")
        
        if player_choice == "rock":
            self.evaluate_against_rock(opponent_choice)
        elif player_choice == "paper":
            self.evaluate_against_paper(opponent_choice)
        else:
            self.evaluate_against_scissors(opponent_choice)

        
    def evaluate_against_rock(self, opponent_choice: str) -> None:
        if opponent_choice == "rock":
            print("\nThis round ended in a tie!")
            self.add_tie()
        elif opponent_choice == "paper":
            print("\nYou lost this round!")
            self.add_opponent_point()
        else:
            print("\nYou win this round!")
            self.add_player_point()
    
    
    def evaluate_against_paper(self, opponent_choice: str) -> None:
        if opponent_choice == "rock":
            print("\nYou win this round!")
            self.add_player_point()
        elif opponent_choice == "paper":
            print("\nThis round ended in a tie!")
            self.add_tie()
        else:
            print("\nYou lost this round!")
            self.add_opponent_point()

    
    def evaluate_against_scissors(self, opponent_choice: str) -> None:
        if opponent_choice == "rock":
            print("\nYou lost this round!")
            self.add_opponent_point()
        elif opponent_choice == "paper":
            print("\nYou win this round!")
            self.add_player_point()
        else:
            print("\nThis round ended in a tie!")
            self.add_tie()

    
    def play_again_prompt(self):
        choice = input("\nWould you like to play again: ").lower()
        if choice in self.quit_options[:2]:
            self.run_game_loop()
        else:
            self.is_running = not self.is_running