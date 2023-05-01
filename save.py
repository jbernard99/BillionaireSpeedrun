import json

def save(usdollars):
	file = open("save.json", "w")
	data = {"usdollars": usdollars}
	json.dump(data, file)
	file.close()

def load_data():
	try:
		file = open("save.json", "r")
	except:
		save(0)
		return (0)
	else:
		data = json.load(file)
		file.close()
		return (data["usdollars"])