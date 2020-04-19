import constants


def sort_players():
    run = True

    # Make a copy of teams and players so we don't modify constants in any way like it says not to...
    teams = constants.TEAMS[::]
    players = constants.PLAYERS[::]

    # Get length of teams and number of players
    length_of_teams = len(teams)
    num_of_player = len(players)

    # Calculate how many players should be on each team so this can be reused in case constants.py changes
    players_per_team = num_of_players_per_team = num_of_player / length_of_teams

    # Store team data here
    teams_with_players = {}
    # Model = { "team Name" : [ {playerInfo}, {PlayerInfo} ], "team Name" : [ {playerInfo}, {PlayerInfo} ], ... }

    # Adds each team name as a key to teams_with_players
    for team in teams:
        teams_with_players[team] = []

    # Split players into even teams
    players_with_exp = []
    players_without_exp = []

    for player in players:
        if(player['experience'] == 'YES'):
            players_with_exp.append(player)
        else:
            players_without_exp.append(player)

    exp_players_per_team = len(players_with_exp)/length_of_teams

    # Assign players with experience  <======================= BALANCING EXPERIENCED vs INEXPERIENCED PLAYERS FOR EXCEEDS
    team_index = 0
    for player in players_with_exp:
        if(len(teams_with_players[teams[team_index]]) == exp_players_per_team):
            team_index += 1
        curr_team = teams_with_players[teams[team_index]]
        curr_team.append(player)

    # Assign players without experience  <======================= BALANCING EXPERIENCED vs INEXPERIENCED PLAYERS FOR EXCEEDS
    team_index = 0
    for player in players_without_exp:
        if(len(teams_with_players[teams[team_index]]) == players_per_team):
            team_index += 1
        curr_team = teams_with_players[teams[team_index]]
        curr_team.append(player)

    # Alter player data (Height => int; Experience => Bool; Guardians => list of strings) <======================= CLEANING DATA FOR EXCEEDS
    for team in teams_with_players:
        for y, player in enumerate(teams_with_players[team]):
            # Change height to int
            teams_with_players[team][y]['height'] = int(
                teams_with_players[team][y]['height'][:2])

            # Convert guardians string to a list of strings
            teams_with_players[team][y]['guardians'] = teams_with_players[team][y]['guardians'].split(
                ' and')

            # Change experience to bool
            if(teams_with_players[team][y]['experience'] == 'NO'):
                teams_with_players[team][y]['experience'] = False
            else:
                teams_with_players[team][y]['experience'] = True

    print('\nBASKETBALL TEAM STATS TOOL\n')

    while run:  # <======================= WILL RE-PROMPT PLAYERS WITH MENU UNTIL PLAYER QUITS
        print('====MENU====')
        print('\nHere are your choices:')
        print('1) Display Stats')
        print('2) Quit\n')

        while run:
            try:
                user_option_choice = int(input('Enter An Option --> '))
                if (user_option_choice == 1):
                    print('\n --Teams--')
                    for index, team in enumerate(teams):
                        print(str(index + 1) + ') ' + str(team))
                    while run:
                        try:
                            get_team_choice = int(
                                input('\nChoose A Team --> '))

                            # Handle Error if user chooses number that is not an option
                            if(not(1 <= get_team_choice <= len(teams))):
                                print("That's not a valid option")
                                break

                            team_index_chosen = get_team_choice - 1
                            # Print Team Name
                            print("\nTeam: " +
                                  teams[team_index_chosen] + ' Stats')
                            print("--------------------")

                            # Total Players
                            print("Number Of Players: " +
                                  str(len(teams_with_players[teams[team_index_chosen]])))

                            # Total experienced
                            print('Total Experienced Players: ' +
                                  str(int(exp_players_per_team)))

                            # Total inexperienced
                            print('Total Inexperienced Players: ' +
                                  str(int(players_per_team - exp_players_per_team)))

                            # avg height
                            height = 0
                            for player in teams_with_players[teams[team_index_chosen]]:
                                height += player['height']
                            print('Average Height: ' +
                                  str(height/players_per_team) + '\"')

                            # Print players on team
                            print('\nPlayers On Team: ')
                            players_on_team = []
                            for player in teams_with_players[teams[team_index_chosen]]:
                                players_on_team.append(player['name'])
                            print('  ' + ', '.join(players_on_team))
                            print('')

                            # Print list of guardians
                            guardians_list = []
                            for player in teams_with_players[teams[team_index_chosen]]:
                                guardians_list += player['guardians']
                            print('Player Guardians: ' +
                                  ', '.join(guardians_list) + '\n')
                            guardians_list = []

                            break

                        except ValueError:
                            print('Error: Please use only numbers')
                    break
                elif user_option_choice == 2:
                    print("Goodbye")
                    run = False
                else:
                    print("That's not a valid choice")
            except ValueError:
                print('Error: Please use only numbers\n')


if __name__ == '__main__':
    sort_players()
