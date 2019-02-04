users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

def num_friends(user_id):
    '''
    Find number of friends for a given user
    '''
    num_of_friends = 0
    
    for f in friendship:
        if user_id in f:
            num_of_friends = num_of_friends + 1

    return num_of_friends

def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
    '''
    friends_list = []
    for u in users:
        temp_li = [u["name"], num_friends(u["id"])]
        friends_list.append(temp_li) 
    
    sorted_list = sorted(friends_list,key=lambda l:l[1], reverse=True)
    for li in sorted_list:
        print("User %s has %d friends." % (li[0], li[1]))
        

print("Sorting by number of friends")
sort_by_num_friends()


print("")
user_ = 1
print("Calculating nuber of friends for user %s" % user_)
num_friends = num_friends(user_)
print("User %d has %d friends" % (user_, num_friends))


