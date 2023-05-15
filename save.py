import json

def save(usdollars, bitcoin, ebook):
	file = open("save.json", "w")
	data = {"usd": usdollars, "btc": bitcoin, "ebook": ebook}
	json.dump(data, file)
	file.close()

def load_data():
	try:
		file = open("save.json", "r")
	except:
		save(0, 0, 0)
		return (0, 0, 0)
	else:
		data = json.load(file)
		file.close()
		if len(data.items()) != 3:
			save(0, 0, 0)
		return (data["usd"], data["btc"], data["ebook"])