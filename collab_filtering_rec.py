""" Python warm-up! """

# Store user ratings
user_ratings = {"Elissa": {"Leaf Shorts": 5, "Floral Shorts": 5},
                "Erin": {"Leaf Shorts": 2, "Floral Shorts": 5},
                "Stella": {"Leaf Shorts": 4, "Floral Shorts": 1}
                }

# Print Stella's ratings.
print user_ratings['Stella']

# What did Elissa think of those floral ones?
print user_ratings['Elissa']['Leaf Shorts']

def what_did_they_think(rating):
  if rating > 3:
    opinion = "LOVED IT!"
  else: 
    opinion = "HATED IT!"
  return opinion

my_humble_opinion = what_did_they_think(user_ratings['Erin']['Leaf Shorts'])

print "Erin's review of the Leaf Shorts: " + my_humble_opinion

""" Let's get serious. """

def compute_manhattan_distance(user_rating1, user_rating2): 
  """ 
      This function computes the Manhattan distance between two user's 
      ratings.  Both arguments should be dictionaries keyed on users, 
      and items.
  """
  distance = 0
  for key in user_rating1:
    if key in user_rating2:
      distance += abs(user_rating1[key] - user_rating2[key])
  return distance

def find_nearest_neighbor(username, users):
  """ 
  """
  distances = []
  for user in users:
    if user != username:
      distance = compute_manhattan_distance(users[user], users[username])
      distances.append((distance, user))
  distances.sort()
  return distances[0]
      
def get_recommendations(username, users):
  """
  """
  nearest_user = find_nearest_neighbor(username, users)
  recommendations = []

  neighbor_ratings = user[nearest_user]


