#Using functions generate a trophy based on hours spent playing a game

def get_time_trophy(hours_played):

    if hours_played >= 50:
        trophy_name = "Valiant Veteran"
    elif hours_played >=24:
        trophy_name="Humble Hero"
    elif hours_played >= 10:
        trophy_name = "Active Adventurer"
    else:
        trophy_name = "Trainee Traveller"
    return trophy_name

print (get_time_trophy(2))
print (get_time_trophy(11))
print (get_time_trophy(33))
print (get_time_trophy(55))