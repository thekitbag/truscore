class Test():

	def getResults():
		results = [
		{"uuid":101, "type": "Hotel", "name": "Sol Sirenas Coral", "score": "22(1097)"},
		{"uuid":234, "type": "Hotel", "name": "Melia Internacional", "score": "74(588)"},
		{"uuid":696, "type": "Hotel", "name": "Playa del Mar", "score": "38(77)"}
		]
		return results

	def getMoreInfo():		
		"""call db with uuid and retreive ore info and return json"""
		more_info = {
		"trend": {"current": 22, "1w": 24, "1m": 26, "3m":26, "6m": 26, "1y": 30, "2y": 45},
		"recent votes": {"John Doe(987)": "1*", "Migulito(13)": "5*", "Pavel13": "2*"},
		"best bits": {"Beach": 9, "Pool":7, "Staff":3},
		"worst bits": {"Food": 28, "Staff": 14, "cleanliness": 10},
		"selected comments": 
			[{"name": "John Doe", "user reliability": 85, "date": "November 15th 2018", "comment": "Don't go here if you want to drink beer. Food also inedible."}]
		}
		return more_info

