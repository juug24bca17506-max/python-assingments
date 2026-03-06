"""
Aim: Write a Program to implement control flow statements and looping statements in python.
"""

n = int(input("Enter the number of players: "))

for i in range(n):

    print("\nPlayer", i + 1)

    runs = int(input("Enter the runs scored: "))
    balls = int(input("Enter the number of balls faced: "))
    fours = int(input("Enter the number of 4s scored: "))
    sixes = int(input("Enter the number of 6s scored: "))
    wickets = int(input("Enter the number of wickets taken: "))
    runs_conceded = int(input("Enter the number of runs conceded: "))
    overs = int(input("Enter the number of overs bowled: "))
    catches = int(input("Enter the number of catches taken: "))

    strike_rate = (runs / balls) * 100
    economy = runs_conceded / overs

    # Batting Performance
    if runs >= 50 and strike_rate >= 120:
        batter = "Excellent Batter"
    elif runs >= 30 and strike_rate >= 100:
        batter = "Good Batter"
    elif runs >= 20:
        batter = "Average Batter"
    else:
        batter = "Poor Batter"

    # Bowling Performance
    if wickets >= 3 and economy <= 6:
        bowler = "Excellent Bowler"
    elif wickets >= 2 and economy <= 8:
        bowler = "Good Bowler"
    elif wickets >= 1:
        bowler = "Average Bowler"
    else:
        bowler = "Poor Bowler"

    # Fielding Performance
    if catches >= 2:
        fielder = "Outstanding Fielder"
    elif catches == 1:
        fielder = "Active Fielder"
    else:
        fielder = "Needs Improvement"

    # Overall Performance
    if batter == "Excellent Batter" and bowler == "Excellent Bowler":
        overall = "Star All-Rounder"
    elif batter == "Good Batter" and bowler == "Good Bowler":
        overall = "Strong All-Rounder"
    elif batter == "Good Batter" or bowler == "Good Bowler":
        overall = "Supporting All-Rounder"
    else:
        overall = "Needs Improvement"

    print("\nStrike Rate:", strike_rate)
    print("Economy:", economy)
    print("Batting:", batter)
    print("Bowling:", bowler)
    print("Fielding:", fielder)
    print("Overall:", overall)