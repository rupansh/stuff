SAVE_NT = True
kekd = dict()
ourd = dict()

def add_prop(prop_line: str, stored: dict):
	if prop_line.lstrip() and prop_line.lstrip()[0] != "#":
		l = prop_line.rstrip().split("#")[0].split("=")
		stored[l[0]] = l[1]

with open("kek.prop", "r") as kek, open("build.prop", "r") as our:
	for line in kek:
		add_prop(line, kekd)
	for line in our:
		add_prop(line, ourd)

with open("system.prop", "w") as new:
	for k in kekd.keys():
		if k in ourd.keys():
			new.write(f"{k}={ourd[k]}\n")
		else:
			if SAVE_NT:
				new.write(f"{k}={kekd[k]}\n")

			print("WARN: Key", k, "not in our build.prop!")
