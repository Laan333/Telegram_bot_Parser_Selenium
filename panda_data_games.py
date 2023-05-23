import pandas
import parser



def create_data():
    dict_of_games = {
        "game":[],
        "href":[]
    }
    parser.create_new_data()
    for i in range(len(parser.name)):
        dict_of_games["game"].append(parser.name[i])
        dict_of_games["href"].append(parser.href[i])
    df = pandas.DataFrame(dict_of_games)
    df.to_csv(f"data_about_games/data_games.csv")


def took_data():
    data = pandas.read_csv("data_about_games/data_games.csv")
    game_name = data["game"].to_list()
    game_link = data["href"].to_list()
    return game_name, game_link

