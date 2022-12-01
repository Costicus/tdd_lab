class Team: 
    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach
        self.points = 0

    def add_player(self, player):
        return self.players.count(player) > 0

    def has_player(self, player):
        for team_member in self.players:
            if player == team_member:
                return True
        else:
            False

    def play_game(self, game_won):
        if game_won:
            self.points += 3
