#using if-else
# player_name = input("Enter player name: ")
# if player_name:
#     player = player_name
# else:
#     player = "Guest Player"
#
# print(f"Welcome, {player}!")

#using "or"
player_name = input("Enter player name: ")
player = player_name or "Guest Player"
print(f"Welcome, {player}!")