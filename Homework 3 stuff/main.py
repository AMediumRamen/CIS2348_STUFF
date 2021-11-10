#Ahmed Rahman PSID:1820239

class Team:
    def __init__(self):
        self.teamName = 'none'
        self.teamWins = 0
        self.teamLosses = 0

    def get_win_percentage(self):
        return self.teamWins/(self.teamWins+self.teamLosses)

if __name__ == "__main__":
    yikes = Team()
    name = input()
    wins = int(input())
    loss = int(input())

    yikes.teamName = name
    yikes.teamWins = wins
    yikes.teamLosses = loss

    if yikes.get_win_percentage()>0.5:
        print('Congratulations, Team',name,'has a winning average!')
    else:
        print('Team',name,'has a losing average.')
