class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.scores = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_tie_score(self, score):
        if score == 0:
            return "Love-All"
        elif score == 1:
            return "Fifteen-All"
        elif score == 2:
            return "Thirty-All"
        else:
            return "Deuce"

    def get_end_game_score(self, difference):
        if difference == 1:
            return f"Advantage {self.player1_name}"
        elif difference == -1:
            return f"Advantage {self.player2_name}"
        elif difference >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def get_player_score_string(self, score):
        return self.scores[score]

    def get_score(self):
        if self.player1_score == self.player2_score:
             score = self.get_tie_score(self.player1_score)

        elif self.player1_score >= 4 or self.player2_score >= 4:
             difference = self.player1_score - self.player2_score
             score = self.get_end_game_score(difference)

        else:
            score = self.get_player_score_string(self.player1_score) + "-" + self.get_player_score_string(self.player2_score)

        return score
