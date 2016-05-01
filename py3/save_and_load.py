import glob
from base64 import a85encode, a85decode

def read_game_data(username):

    filename = "savefile_" + username + ".txt"

    with open(filename, "rb") as f:
        data = f.read()
    data = data[:data.rindex(b';')]

    a85_decoded_data = a85decode(data)
    print('a85_decoded_data:', a85_decoded_data)

    utf8_decoded_data = a85_decoded_data.decode("utf-8")
    print('utf8_decoded_data:', utf8_decoded_data)

    return utf8_decoded_data.split("_")


def encode_and_save(username, data):
    if data is None:
        data = ["auto", 0, "print", 0, "counter", 0, "shares", 0, "bank", 0, "upg1h1", 0, "upg1h2", 0,
                "upg2h1", 0, "upg2h2", 0, "upg3", 0, "upg4", 0, "upg5", 0, "cupg1", 0, "cupg2", 0,
                "money", 0.0, "time", 0, "clicks", 0, "lotto", 100]

    print('saving data:', data)

    underscore_joined = str("_").join(str(y) for y in data)
    print('underscore_joined:', underscore_joined)

    utf8_encoded_data = underscore_joined.encode("utf-8")
    print('utf8_encoded_data:', utf8_encoded_data)

    a85_encoded_data = a85encode(utf8_encoded_data) + b";"
    print('a85_encoded_data:', a85_encoded_data)

    filename = "savefile_" + username + ".txt"
    with open(filename, "wb") as f:
        f.write(a85_encoded_data)

    print('data saved:', data)


def save_file_exists(username):
    return ('savefile_' + username + '.txt') in glob.glob('savefile_*.txt')

