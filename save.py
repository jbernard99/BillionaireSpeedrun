import json

def save(usdollars, bitcoin):
	file = open("save.json", "w")
	data = {"usd": usdollars, "btc": bitcoin}
	json.dump(data, file)
	file.close()

def load_data():
	try:
		file = open("save.json", "r")
	except:
		save(0, 0)
		return (0, 0)
	else:
		data = json.load(file)
		file.close()
		return (data["usd"], data["btc"])