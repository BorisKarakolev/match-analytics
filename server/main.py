import re
filepath = 'data.txt'

rx_data = {
    'teams': re.compile(r'\bTeamVitality\s[6 - 16]\s\bNAVI\sGGBET'),
    'rounds_played': re.compile(r'\bRoundsPlayed:\s22'),
    'all_time': re.compile(r'\b50\smin'),
    'map': re.compile(r'\bde_nuke'),
    # 'terrorists': {
    #         'misutaaa': re.compile(r'misutaaa<24>'),
    #         'apEX': re.compile(r'apEX<25>'),
    #         'ZywOo': re.compile(r'ZywOo<26>'),
    #         'Kyojin': re.compile(r'Kyojin<34>'),
    #         'shox': re.compile(r'shox\s<33>')
    #     },
    # 'CT': {
    #         'Perfecto': re.compile(r'Perfecto<28>'),
    #         'Boombl4': re.compile(r'Boombl4<29>'),
    #         's1mple': re.compile(r's1mple<30>'),
    #         'electronic': re.compile(r'electronic<31>'),
    #         'b1t': re.compile(r'b1t<35>')
    #     }
    # },
    'won': re.compile(r'\bTeam\sTeamVitality\swon')
}


def _parse_line(line):
    for key, rx in rx_data.items():
        print(rx)
        match = rx.search(line)
        if match:
            return key, match

    return None, None


def parse_file(filepath):
    data = {}
    with open(filepath, 'r') as text_file:
        line = text_file.readlines()
        while line:
            key, match = _parse_line(line)

            if key == 'teams':
                setattr(data, 'teams', match.group())

            if key == 'rounds_played':
                setattr(data, 'rounds_played', match.group())

            if key == 'all_time':
                setattr(data, 'all_time', match.group())

            if key == 'map':
                setattr(data, 'map', match.group())
    return data


if __name__ == '__main__':
    data = parse_file(filepath)
    print(data)
