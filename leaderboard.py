import csv
import os
import turtle

TOP_PLAYERS = 5


def _load_high_scores():
    high_scores_in_file = []
    if os.path.exists("high_scores.csv"):
        with open("high_scores.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                player_name, score = row
                high_scores_in_file.append({"player_name": player_name, "score": int(score)})
    return high_scores_in_file


def add_if_high_score(score):
    high_scores = _load_high_scores()
    print(f"len high_scores {len(high_scores)}")

    if len(high_scores) < TOP_PLAYERS or score > high_scores[-1]["score"]:
        player_name = turtle.textinput("Your score is in top 5", "Write your name to save your success")
        high_scores.append({"player_name": player_name, "score": int(score)})
        _add_score_to_file(high_scores)


def _add_score_to_file(high_scores):
    high_scores = _sort_and_cut(high_scores)

    with open("high_scores.csv", "w", newline='') as file:
        writer = csv.writer(file)
        for row in high_scores:
            writer.writerow([row["player_name"], row["score"]])


def _sort_and_cut(high_scores):
    high_scores = sorted(high_scores, key=lambda x: x['score'], reverse=True)
    resized = high_scores[:TOP_PLAYERS]
    return resized


def display_high_scores():
    high_scores = _load_high_scores()
    if high_scores:
        print("High Scores:")
        for i, record in enumerate(high_scores, start=1):
            print(f"{i}. {record['player_name']}: {record['score']}")
    else:
        print("No high scores available.")
