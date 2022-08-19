import re

filepath = 'data.txt'

def parse_file(filepath):
    data = {}
    with open(filepath, 'rt') as text_file:
        contents = text_file.readlines()
        for part in contents:

            teams_score = re.search(r'\bNAVI\sGGBET\s\[6 - 16]\sTeamVitality', part)
            rounds_played = re.search(r'RoundsPlayed: 22', part)
            all_time = re.search(r'50 min', part)
            game_map = re.search(r'de_nuke', part)
            players = re.search(r'21:30:51:\s"[a-zA-Z0-9]+\s?<[0-9]+><STEAM_([0-9]+(:[0-9]+)+)><[A-Z]+>"', part)
            print(players)
            if teams_score:
                data['teams'] = re.findall('NAVI\sGGBET|TeamVitality', teams_score.group())
                data['score'] = re.findall('6 - 16', teams_score.group())[0]
            if rounds_played:
                data['rounds_played'] = re.findall('22', rounds_played.group())[0]
            if all_time:
                data['all_time'] = re.findall('50', all_time.group())[0]
            if game_map:
                data['map'] = game_map.group()
            # if players:
            #      print(players)

    return data

data = parse_file(filepath)
print(data)

# rx_data = {
#     'teams': re.compile(r'\bTeamVitality\s\[6 - 16]\sNAVI\sGGBET'),
#     'rounds_played': re.compile(r'\bRoundsPlayed:\s22'),
#     'all_time': re.compile(r'\b50\smin'),
#     'map': re.compile(r'\bde_nuke'),
#     'won': re.compile(r'\bTeam\sTeamVitality\swon')
# }

# def parse_line(line, rx_dict):
#     for key, rx in rx_dict.items():
#         match = rx.search(line)
#         if match:
#             return key, match

#     return None


# obj = defaultdict(list)
# with open('data.txt', 'r') as f:
#     for line_number, line in enumerate(f):
#         match = parse_line(line, rx_data)
#         if match:
#             # print(
#             #     f'found match at line {line_number}: {match[0]} >> {match[1].group()}')
#             # store line_number and match
#             obj[match[0]].append((match[1].group()))

# print(obj)