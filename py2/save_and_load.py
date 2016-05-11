import glob
import game_model


def auto_updater(g2, un):
    wordlist = ["auto", "print", "counter", "shares", "bank", "upg1h1", "upg1h2", "upg2h1", "upg2h2", "upg3", "upg4",
                   "upg5", "cupg1", "cupg2", "quintillion", "quadrillion", "trillion", "billion", "million", "money",
                   "time", "clicks", "lotto"]
    wordlist2 = []
    for a in range(len(wordlist)):
        for b in range(len(g2)):
            if g2[b] == wordlist[a]:
                wordlist2.extend([wordlist[a], g2[b]])
            else:
                if wordlist[a] == "lotto":
                    wordlist2.extend(["lotto", 1])
                else:
                    wordlist2.extend([wordlist[a], 0])

    return wordlist2


def read_game_data(username):
    filename = "savefile_" + username + ".txt"
    with open(filename) as f:
        data = f.read()
    decoded_data = data.split(";")[0].decode("hex")
    return game_model.GameState(decoded_data.split("_"))


def encode_and_save(username, game_state):
    data = ["auto", game_state.autoclick2, "print", game_state.printmoney2, "counter", game_state.counterfeit2,
            "shares", game_state.sharecrash2, "bank", game_state.bankheist2, "upg1h1", game_state.upgcheck1h1,
            "upg1h2", game_state.upgcheck1h2, "upg2h1", game_state.upgcheck2h1, "upg2h2", game_state.upgcheck2h2,
            "upg3", game_state.upgcheck3, "upg4", game_state.upgcheck4, "upg5", game_state.upgcheck5,
            "cupg1", game_state.clickupgcheck1, "cupg2", game_state.clickupgcheck2, "money",
            game_state.money, "time", game_state.timeplay, "clicks",
            game_state.totalclicks, "lotto", game_state.lottoprice]

    encoded_data = ("_".join(str(v) for v in data)).encode("hex") + ";"

    filename = "savefile_" + username + ".txt"
    with open(filename, "w") as f:
        f.write(encoded_data)


def save_file_exists(username):
    return 'savefile_' + username + '.txt' in glob.glob('savefile_*.txt')

