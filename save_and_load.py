import glob


def read_game_data(username):
    filename = "savefile_" + username + ".txt"
    with open(filename) as f:
        data = f.read()
    decoded_data = data.split(";")[0].decode("hex")
    return decoded_data.split("_")


def encode_and_save(username, data=None):
    if data is None:
        data = ["auto", 0, "print", 0, "counter", 0, "shares", 0, "upg1h1", 0, "upg1h2", 0,
                "upg2h1", 0, "upg2h2", 0, "upg3", 0, "upg4", 0, "cupg1", 0, "cupg2", 0,
                "quintillion", 0, "quadrillion", 0, "trillion", 0, "billion", 0, "million", 0,
                "money", 0.0, "time", 0, "clicks", 0]

    encoded_data = ("_".join(str(v) for v in data)).encode("hex") + ";"

    filename = "savefile_" + username + ".txt"
    with open(filename, "w") as f:
        f.write(encoded_data)


def save_file_exists(username):
    return ('savefile_' + username + '.txt') in glob.glob('savefile_*.txt')

