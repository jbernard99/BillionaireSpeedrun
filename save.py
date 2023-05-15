import json

def save(save_tab):
	file = open("save.json", "w")
	data = {"data": save_tab}
	json.dump(data, file)
	file.close()

def load_data(qtty):
	print(qtty)
	try:
		file = open("save.json", "r")
	except:
		save([0] * qtty)
		return ([0] * qtty)
	else:
		data = json.load(file)
		file.close()
		ret = []
		for saved_item in data.items():
			ret.append(saved_item[1])
		if len(ret) != qtty:
			save([0] * qtty)
		print(ret[0])
		return (ret[0])