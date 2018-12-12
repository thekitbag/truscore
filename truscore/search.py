from random import randint
from datetime import date

class Test():

	def getResults():
		"""interpret search term, use some public API to find hits, look up those hits against votes in the DB,
		run patented Truscore algorithm and return Truscors for them all"""
		results = [
		{"uuid":101, "type": "Hotel", "name": "Sol Sirenas Coral", "score": "22(1097)"},
		{"uuid":234, "type": "Hotel", "name": "Melia Internacional", "score": "74(588)"},
		{"uuid":696, "type": "Hotel", "name": "Playa del Mar", "score": "38(77)"}
		]
		return results

	def getMoreInfo():		
		"""call db with uuid, retrieve more info and return json"""
		more_info = {
		"trend": {"current": 22, "1w": 24, "1m": 26, "3m":26, "6m": 26, "1y": 30, "2y": 45},
		"recent votes": {"John Doe(987)": "1*", "Migulito(13)": "5*", "Pavel13": "2*"},
		"best bits": {"Beach": 9, "Pool":7, "Staff":3},
		"worst bits": {"Food": 28, "Staff": 14, "cleanliness": 10},
		"comments": 
			[{"name": "John Doe", "user reliability": 85, "date": "November 15th 2018", "comment": "Don't go here if you want to drink beer. Food also inedible."}]
		}
		return more_info

	def sendRating():
		"""record rating in the DB"""
		return "rating submitted"

	def calculateTrueScore(votes):
		"""takes a list of dictionaries, votes, looks at the relevant details and returns a score"""
		weighted_votes = []
		for vote in votes:
			date = vote['date']
			user = vote['user']
			value = vote['score']			
			weight = Test.calculateVoteWeight(date, user, value)
			weighted_votes.append({"date": date, "user": user, "value": value, "weight": weight})
		print(weighted_votes)
		number_of_votes = len(weighted_votes)
		aggregate_score = 0
		effective_number_of_votes = 0
		for entry in weighted_votes:
			effective_number_of_votes += entry['weight']
			product = entry['value'] * entry['weight']
			aggregate_score += product
		truescore = aggregate_score/effective_number_of_votes
		return str(truescore) + " (" + str(number_of_votes) + ")"


	def calculateVoteWeight(date, user, vote_value):
		"""takes the date of a vote and who cast it and gives it a weight from 0 to 100"""
		personality = Test.calculateUserPersonality(user)
		date_score = Test.calculateDateWeighting(date)
		if vote_value < 2.5 and personality > 0:
			personality_score = 2
		elif vote_value > 2.5 and personality < 0:
			personality_score = 2
		vote_weight = personality_score * date_score
		print("vote weight:", vote_weight)
		return vote_weight

	def calculateUserPersonality(username):
		"""returns a number from X to Y indicating the users tendency for positive or negative votes"""
		user = User.getUserByUsername(username)
		average_vote = float(sum(user.votes)) / len(user.votes)
		if average_vote < 2:
			return -2
		elif average_vote < 3:
			return -1
		elif average_vote < 4:
			return 1
		elif average_vote < 5:
			return 2

	def days_ago(year, month, day):
		input_date = date(year, month, day)
		today = date.today()
		delta = today - input_date
		return delta.days 

	def calculateDateWeighting(date):
		year = int(date[0:4])
		month = int(date[5:7])
		day = int(date[8:10])
		days_since_vote = Test.days_ago(year,month,day)
		if days_since_vote < 7:
			return 1
		elif days_since_vote < 21:
			return 0.75
		elif days_since_vote < 50:
			return 0.50
		elif days_since_vote < 100:
			return 0.25

 

test_votes = [
{'date': '2018-11-27', 'user':'mark', 'score':2},
{'date': '2018-10-23', 'user':'paul', 'score':5}
]

positive_votes = [3,4,4,5,4,4,5]
negative_votes = [1,2,2,1,2]

 
users = []
 

class User():
	def __init__(self):
		self.name = ""
		self.votes = []

	def getUserByUsername(username):
		user = [userObject for userObject in users if userObject.name == username]
		return user[0]

 

mark = User()
mark.name = "mark"
mark.votes = positive_votes
paul = User()
paul.name = "paul"
paul.votes = negative_votes
users.append(mark)
users.append(paul)


print(Test.calculateTrueScore(test_votes))
