import csv
import os
import turtle

TOP_PLAYERS = 5


def _load_high_scores():
    """
    Saves score board from the file into a list
    :return: List[Dict["player_name" = str,"score" = int]]
    """
    high_scores_in_file = []
    if os.path.exists("high_scores.csv"):
        with open("high_scores.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                player_name, score = row
                high_scores_in_file.append({"player_name": player_name, "score": int(score)})
    return high_scores_in_file


def add_if_high_score(score):
    """
    Adds the score from the finished game to the leaderboard if it's high enough

    Score is high enough if it's higher than the last score of the leaderboard,
    or if the leaderboard is not yet full

    :param score: final score at the end of a game session
    """

    # read score table into a local list
    high_scores = _load_high_scores()

    # the score is put into the leaderboard if the leaderboard is not yet full,
    # or if it's higher than the last one in the leaderboard
    if len(high_scores) < TOP_PLAYERS or score > high_scores[-1]["score"]:
        # prompt is displayed to ask player for the name
        player_name = turtle.textinput("Your score is in top 5", "Write your name to save your success")
        # if no name is given, then default string "___" is subsidized
        if player_name is None or len(player_name) == 0:
            player_name = "___"
        # long names are cut to fit on screen
        if len(player_name) > 10:
            player_name = player_name[:10]
        high_scores.append({"player_name": player_name, "score": int(score)})
        # name and score are added to the leaderboard file
        _add_score_to_file(high_scores)


def _add_score_to_file(high_scores):
    """
    Stores high scores in the correct order in the high_score file

    Local list with high scores is sorted, so the newly added high score is at the right place
    :param high_scores: unsorted list of leaderboard members

    """
    # sort the local list
    high_scores = _sort_and_cut(high_scores)

    # rewrite the storing file
    with open("high_scores.csv", "w", newline='') as file:
        writer = csv.writer(file)
        for row in high_scores:
            writer.writerow([row["player_name"], row["score"]])


def _sort_and_cut(high_scores):
    """
    Sorts local list of high scores, cuts it to the number of leaderboard members (default 5)
    :param high_scores:
    :return: standardized sorted leaderboard list
    """
    high_scores = sorted(high_scores, key=lambda x: x['score'], reverse=True)
    resized = high_scores[:TOP_PLAYERS]
    return resized


def score_lines():
    """
    Makes a formatted string from the leaderboard elements
    :return: String
    """
    high_scores = _load_high_scores()
    lines = ""

    # each line of the leaderboard is added to the string, separated by "\n" element
    for i, record in enumerate(high_scores, start=1):
        line = f"{i}.{record['player_name']} {record['score']}\n"
        lines += line

    return lines



