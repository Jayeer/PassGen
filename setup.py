import os

ignore = ["README.md", ".git", ".gitignore", "setup.py"]

def copy_to_share():
	if not os.path.exists("/usr/share/passgen"):
		os.mkdir("/usr/share/passgen")

	for file in os.listdir("."):
		if (file in ignore):
			continue
		if (os.path.isdir(file)):
			continue
		local_file = open(file, "r")
		global_file = open(os.path.join("/usr/share/passgen", file), "w")
		global_file.write(local_file.read())
		global_file.close()
		local_file.close()

def create_link():
	fd = open("/usr/bin/passgen", "w")
	fd.write("#! /usr/bin/bash\n")
	fd.write("cd /usr/share/passgen && python3 main.py")
	fd.close()
	os.chmod("/usr/bin/passgen", 0o755)


def main():
	print("Installation started")
	print("Copying to /usr/share")
	copy_to_share()
	print("Copied")
	print("Creating link in /usr/bin")
	create_link()
	print("Created")
	print("Installation finished")


if __name__ == "__main__":
	main()