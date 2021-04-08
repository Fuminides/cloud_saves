'''
Author: Javier Fumanal Idocin
javierfumanalidocin at gmail dot com

Module to handle persistence for the library
'''

import json

basic_conf = './my_conf.json'

def load_games():
    try:
        f = open(basic_conf, "r")
    except FileNotFoundError:
        f = open(basic_conf, "w")
        f.write('{}')
        f.close()
        f = open(basic_conf, "r")

    games = json.load(f)
    f.close()

    return games


def add_game(name, origin, sync):
    games = load_games()
    games[name] = [origin, sync]
    json_string = json.dumps(games)
    f = open(basic_conf, "w")
    f.write(json_string)
    f.close()
