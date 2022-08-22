from flask import Flask
from flask_cors import CORS
import re

filepath = 'data.txt'
app = Flask(__name__)
CORS(app)

def parse_file(filepath):
    data = {}
    players_array = []
    terrorists = []
    ct = []
    with open(filepath, 'r') as text_file:
        lines = text_file.readlines()
        for part in lines:

            teams_score = re.search(
                r'\bNAVI\sGGBET\s\[6 - 16]\sTeamVitality', part)
            rounds_played = re.search(r'RoundsPlayed: 22', part)
            all_time = re.search(r'50 min', part)
            game_map = re.search(r'de_nuke', part)
            won = re.search(r'Team TeamVitality won.', part)
            players = re.search(r'21:30:51:\s"[a-zA-Z0-9]+\s?<[0-9]+><STEAM_([0-9]+(:[0-9]+)+)><[A-Z]+>"', part)

            if teams_score:
                data['teams'] = re.findall('NAVI\sGGBET|TeamVitality', teams_score.group())
                data['score'] = re.findall('6 - 16', teams_score.group())[0]
            if rounds_played:
                data['rounds_played'] = re.findall('22', rounds_played.group())[0]
            if all_time:
                data['all_time'] = re.findall('50', all_time.group())[0]
            if game_map:
                data['map'] = game_map.group()
            if won:
                data['won'] = won.group()
            if players:
                players_array.append(players.group())

                for player in players_array:
                    if re.findall('TERRORIST', player):

                        name = re.search(r'[a-zA-Z]+\s?<', player).group()
                        kills = re.search(r'<[0-9]+>', player).group()
                        obj = {'name': re.search(r'[a-zA-Z]+', name).group(), 'kills': re.search(r'[0-9]+', kills).group()}

                        if obj not in terrorists:
                            terrorists.append(obj)

                    else:
                        name = re.search(r'[a-zA-Z0-9]+<', player).group()
                        kills = re.search(r'<[0-9]+>', player).group()
                        obj = {'name': re.search(r'[a-zA-Z0-9]+', name).group(), 'kills': re.search(r'[0-9]+', kills).group()}

                        if obj not in ct:
                            ct.append(obj)

        if terrorists or ct:
            data['players'] = {
                'terrorists': terrorists,
                'ct': ct
            }

        if data['all_time'] and data['rounds_played']:
            data['avg_round_length'] = str((int(data['all_time']) + int(data['rounds_played'])) / 2).split('.')[0]

    return data


@app.route('/', methods=["GET"])
def send_data():
  return parse_file(filepath)

if __name__ == "__main__":
    app.run("localhost", 4200)
