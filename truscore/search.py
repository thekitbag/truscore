from random import randint
from datetime import date
from .models import Vote

class AggregateResults():
	def collateResults(query):
		"""returns all results for a given query"""
		votes = Vote.query.all()
		results = []
		establishments = set()
		for vote in votes:
			establishments.add(vote.establishment)
		for establishment_name in establishments:
			resultData = {}
			resultData['establishment'] = establishment_name
			resultData['truscore'] = Truscore.calculateTruscore(votes, establishment_name)
			results.append(resultData)
		return results


class Truscore():
	def calculateTruscore(votes, establishment_name):
		"""takes a list of vote objects  and an establishment name and returns a weighted score based 
		on the properties of those votes"""
		votes_and_weightings = []
		number_of_votes = 0
		users_and_weights = Truscore.calculateUserWeightings(votes)	
		for vote in votes:
			if vote.establishment == establishment_name:
				number_of_votes += 1
				vote_weight = DateWeight.calculateDateWeighting(vote) * users_and_weights[vote.username]
				vote_dict = {}
				vote_dict['vote value'] = vote.vote
				vote_dict['vote weight'] = vote_weight
				votes_and_weightings.append(vote_dict)	
		totalscore = 0
		effective_number_of_votes = 0
		for item in votes_and_weightings:
			totalscore += (item['vote value'] * item['vote weight'])			
			effective_number_of_votes += item['vote weight']						
		initial_score = totalscore / effective_number_of_votes * 20
		truscore = round(Truscore.adjustForNumberOfVotes(initial_score, number_of_votes))
		return {'score':truscore, 'number of votes':number_of_votes}

	def calculateUserWeightings(votes):
		users_and_weights = {}
		users =  set()
		for vote in votes:
			users.add(vote.username)
		for username in users:
			total_votes = 0
			voter_weight = 0
			for each_vote in votes:
				if each_vote.username == username:
					total_votes += 1
			if total_votes < 5:
				voter_weight = 1
			elif total_votes < 10:
				voter_weight = 2
			elif total_votes < 25:
				voter_weight = 3
			else: vote_weight = 5
			users_and_weights[username] = voter_weight
		return users_and_weights

	def adjustForNumberOfVotes(initial_score, number_of_votes):
		diff = 50-initial_score
		if number_of_votes < 5:
			new_diff = diff/1.5
		elif number_of_votes < 10:
			new_diff = diff/1.3
		elif number_of_votes < 25:
			new_diff = diff/1.1
		else: new_diff = diff
		new_score = 50 - new_diff
		return new_score 

class DateWeight():
	def days_ago(year, month, day):
		input_date = date(year, month, day)
		today = date.today()
		delta = today - input_date
		return delta.days 

	def calculateDateWeighting(vote):
		year = int(vote.date[0:4])
		month = int(vote.date[5:7])
		day = int(vote.date[8:10])
		days_since_vote = DateWeight.days_ago(year,month,day)
		if days_since_vote < 7:
			return 5
		elif days_since_vote < 21:
			return 4
		elif days_since_vote < 50:
			return 3
		elif days_since_vote < 100:
			return 2
		else: return 1

class UserWeight():
	def calculateUserWeighting(vote):
		"""takes the username of a voter and calculates the weight that user deserves based  on
		how many votes they have ever cast and their personality
		n.b. Will need a better way to do this in future as it will currnely query the entire 
		DB for each individual vote - doesn't scale"""
		return 1



class Test():
	def calculateTruscore(establishment):
		return 42

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
		user_score = Test.calculateUserReliability(user)
		if vote_value < 2.5 and personality > 0:
			personality_score = 2
		elif vote_value > 2.5 and personality < 0:
			personality_score = 2
		else: personality_score = 1
		vote_weight = personality_score * date_score * user_score
		print("user:", user, "overall vote weight:", vote_weight)
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

	def calculateUserReliability(username):
		user = User.getUserByUsername(username)
		number_of_votes = len(user.votes)
		if number_of_votes < 5:
			reliability = 0.25
		elif number_of_votes < 20:
			reliability = 1
		elif number_of_votes < 50:
			reliability = 2
		return reliability







