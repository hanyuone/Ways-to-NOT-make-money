import glob
from base64 import a85encode, a85decode

def read_game_data(username):
    filename = "savefile_" + username + ".txt"
    with open(filename, "rb") as f:
        data = f.read().split(b';')[0]
    decoded_data = a85decode(data).decode("utf-8")
    return decoded_data.split("_")


def encode_and_save(username, data):
    if data is None:
        data = ["auto", 0, "print", 0, "counter", 0, "shares", 0, "bank", 0, "upg1h1", 0, "upg1h2", 0,
                "upg2h1", 0, "upg2h2", 0, "upg3", 0, "upg4", 0, "upg5", 0, "cupg1", 0, "cupg2", 0,
                "quintillion", 0, "quadrillion", 0, "trillion", 0, "billion", 0, "million", 0,
                "money", 0.0, "time", 0, "clicks", 0, "lotto", 100]

    encoded_data = a85encode(str("_").join(str(y) for y in data).encode("utf-8")) + b";"

    filename = "savefile_" + username + ".txt"
    with open(filename, "wb") as f:
        f.write(encoded_data)


def save_file_exists(username):
    return ('savefile_' + username + '.txt') in glob.glob('savefile_*.txt')

