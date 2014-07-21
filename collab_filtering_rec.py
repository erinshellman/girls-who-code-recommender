""" Python warm-up! """

# Store user ratings
user_ratings = {"Elissa": {"Leaf Shorts": 5, "Floral Shorts": 5},
                "Erin": {"Leaf Shorts": 2, "Floral Shorts": 5, "Jungle Shorts": 4},
                "Stella": {"Leaf Shorts": 4, "Floral Shorts": 1},
                "Justin": {"Leaf Shorts": 1, "Floral Shorts": 4}
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

def compute_distance(user1_ratings, user2_ratings): 
  """ 
      This function computes the distance between two user's 
      ratings.  Both arguments should be dictionaries keyed on users, 
      and items.
  """
  distances = []
  for key in user1_ratings:
    if key in user2_ratings:
      distances.append((user1_ratings[key] - user2_ratings[key]) ** 2)
  total_distance = round(sum(distances) ** 0.5, 2)
  return total_distance

def find_nearest_neighbors(username, user_ratings):
  """ 
      Returns the list of neighbors, ordered by distance.  
      Call like this: find_nearest_neighbor('Erin', user_ratings)
  """
  distances = []
  for user in user_ratings:
    if user != username:
      distance = compute_distance(user_ratings[user], user_ratings[username])
      distances.append((distance, user))
  distances.sort()
  return distances

def get_recommendations(username, user_ratings):
  """
      Return a list of recommendations.
  """
  nearest_users = find_nearest_neighbors(username, user_ratings)
  recommendations = []

  # Input user's ratings
  ratings = user_ratings[username]

  for neighbor in nearest_users:
    neighbor_name = neighbor[1]
    for item in user_ratings[neighbor_name]:
      if not item in ratings:
        recommendations.append((item, user_ratings[neighbor_name][item]))

  return sorted(recommendations, 
                key = lambda personTuple: personTuple[1],
                reverse = True)

print get_recommendations("Justin", user_ratings)
