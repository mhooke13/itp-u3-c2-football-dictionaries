#from squads_data import SQUADS_DATA

def players_as_dictionaries(squads_list):
    results = []
    for squad in squads_list:
        player = {}

        player.setdefault('number', squad[0])
        player.setdefault('position', squad[1])
        player.setdefault('name', squad[2])
        player.setdefault('date_of_birth', squad[3])
        player.setdefault('caps', squad[4])
        player.setdefault('club', squad[-4])
        player.setdefault('country', squad[-3])
        player.setdefault('club_country', squad[-2])
        player.setdefault('year', squad[-1])
        results.append(player)
        
    return (results)

#x = players_as_dictionaries(SQUADS_DATA)
#print(x)
