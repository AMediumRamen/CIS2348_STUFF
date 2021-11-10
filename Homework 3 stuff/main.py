#Ahmed Rahman PSID:1820239

#Ahmed Rahman PSID:1820239

class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        try:
            return self.team_wins/(self.team_wins+self.team_losses)
        except ZeroDivisionError:
            return 0


if __name__ == "__main__":
    yikes = Team()
    name = input()
    wins = int(input())
    loss = int(input())

    yikes.team_name = name
    yikes.team_wins = wins
    yikes.team_losses = loss

    if yikes.get_win_percentage()>=0.5:
        print('Congratulations, Team',name,'has a winning average!')
    else:
        print('Team',name,'has a losing average.')

