def calculate_gst(value):
    return value * 0.1


team_winnings = [195, 182, 120, 133, 183, 193, 203, 178, 201, 169, 198, 180]
team_sizes = [10, 4, 7, 8, 0, 4, 5, 7, 3, 8, 12]

# Calculate the money won per player in each team
money_per_player = []
for i in range(len(team_winnings)):
    money_per_player.append(team_winnings[i]/team_sizes[i])

# Now calculate the tax each person pays
tax_per_player = []
for money in money_per_player:
    tax_per_player.append(calculate_gst(money))

# Display the results
for i in range(len(team_winnings)):
    print('Players from team', i)
    print('each get $' + str(money_per_player[i] + ' and must pay tax of' + str(tax_per_player[i])))
    print()
