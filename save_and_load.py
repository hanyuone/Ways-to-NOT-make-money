import glob
import game_model
try:
    from base64 import a85encode, a85decode
except ImportError:
    from base64 import b64encode as a85encode
	from base64 import b64decode as a85decode

def read_game_data(username):

    filename = "savefile_" + username + ".txt"

    with open(filename, "rb") as f:
        data = f.read()

    data = data[:data.rindex(b';')]

    utf8_decoded_data = a85decode(data).decode("utf-8")
    print('utf8_decoded_data:', utf8_decoded_data)

    return game_model.GameState(utf8_decoded_data.split("_"))


def encode_and_save(username, game_state):
    data = ["auto", game_state.autoclick2, "print", game_state.printmoney2, "counter", game_state.counterfeit2,
            "shares", game_state.sharecrash2, "bank", game_state.bankheist2, "upg1h1", game_state.upgcheck1h1,
            "upg1h2", game_state.upgcheck1h2, "upg2h1", game_state.upgcheck2h1, "upg2h2", game_state.upgcheck2h2,
            "upg3", game_state.upgcheck3, "upg4", game_state.upgcheck4, "upg5", game_state.upgcheck5,
            "cupg1", game_state.clickupgcheck1, "cupg2", game_state.clickupgcheck2, "money",
            game_state.money, "time", game_state.timeplay, "clicks",
            game_state.totalclicks, "lotto", game_state.lottoprice]

    print('saving data:', data)

    utf8_encoded_data = str("_").join(str(y) for y in data).encode("utf-8")
    print('utf8_encoded_data:', utf8_encoded_data)

    a85_encoded_data = a85encode(utf8_encoded_data) + b";"
    print('a85_encoded_data:', a85_encoded_data)

    filename = "savefile_" + username + ".txt"
    with open(filename, "wb") as f:
        f.write(a85_encoded_data)

    print('data saved:', data)


def save_file_exists(username):
    return ('savefile_' + username + '.txt') in glob.glob('savefile_*.txt')

