def badge_maker(name):
    name_string = f"Hello, my name is {name}."
    return name_string

def batch_badge_creator(names):
    names_list = []
    for name in names:
        names_list.append(f"Hello, my name is {name}.")
    return names_list
    
def assign_rooms(names):
    names_list = []
    i = 1
    for name in names:
        names_list.append(f'Hello, {name}! You\'ll be assigned to room {i}!')
        i += 1
    return names_list

def printer(names):
    badges = batch_badge_creator(names)
    assignments = assign_rooms(names)

    for badge in badges:
        print(badge)
    
    for assignment in assignments:
        print(assignment)
    
