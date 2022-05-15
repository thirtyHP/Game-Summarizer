import os

def load_points_file(players):

    team_one = ''
    team_one_points = 0
    team_two = ''
    team_two_points = 0
    first_scorer = ''
    last_scorer = ''
    total_scorers = 0

    validated = False
    while validated != True:
        logfile = input("Please enter name of log file?")
        path_to_file = './' + logfile
        if os.path.isfile(path_to_file):
                validated = True
        else:
            print ("You must enter the name of a valid .txt file. Please re-enter")

    with open(logfile) as f:
        lines = f.readlines()
        for line in lines:
            line_split = line.split(' ')

            the_team = line_split[0].strip('\n')
            if team_one == '':
                team_one = the_team
            elif team_two == '' and the_team != team_one and the_team != team_two:
                team_two = the_team

            if team_one == the_team:
                team_one_points = team_one_points + int(line_split[2])
            else:
                team_two_points = team_two_points + int(line_split[2])

            the_player = line_split[1].strip('\n')
            if first_scorer == '':
                first_scorer = the_player
            last_scorer = the_player

            if the_player not in players:
                players.append( the_player)
    f.close()
    print(players)
    total_scorers = len(players)
    output_text = ''

    summary_file = open('summary.txt', 'w')

    if team_one_points > team_two_points:
        output_text = team_one + ' won!\n'
        print(output_text)
        summary_file.write(output_text)

    else:
        output_text = team_two + ' won!\n'
        print(output_text)
        summary_file.write(output_text)

    output_text = team_one + ' scored ' + str(team_one_points) + ' points.\n'
    print(output_text)
    summary_file.write(output_text)


    output_text = team_two + ' scored ' + str(team_two_points) + ' points.\n'
    print(output_text)
    summary_file.write(output_text)

    output_text = str(total_scorers) + ' players scored.\n'
    print(output_text)
    summary_file.write(output_text)

    output_text = first_scorer + ' scored first\n'
    print(output_text)
    summary_file.write(output_text)

    output_text = last_scorer + ' scored last\n'   
    print(output_text)
    summary_file.write(output_text)

    summary_file.close()


def main():

    players = []

    load_points_file(players)

main()