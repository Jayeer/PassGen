import os

ignore = ["README.md", ".git", ".gitignore", "setup.py"]

install_dir = "/usr/local/passgen"

def copy_to_share():
	if not os.path.exists(install_dir):
		os.mkdir(install_dir)

	for file in os.listdir("."):
		if (file in ignore):
			continue
		if (os.path.isdir(file)):
			continue
		local_file = open(file, "r")
		global_file = open(os.path.join(install_dir, file), "w")
		global_file.write(local_file.read())
		global_file.close()
		local_file.close()

def create_link():
	fd = open("/usr/bin/passgen", "w")
	fd.write("#! /usr/bin/bash\n")
	fd.write("cd " + install_dir + " && python3 main.py")
	fd.close()
	os.chmod("/usr/bin/passgen", 0o755)
	os.chown(install_dir, os.getuid(), -1)
	os.chown(os.path.join(install_dir, "main.py"), os.getuid(), -1)
	if not os.path.exists("dictionaries"):
		os.mkdir("dictionaries")
	os.chown(os.path.join(install_dir, "dictionaries"), os.getuid(), -1)


def main():
	print("Installation started")
	print("Copying to " + install_dir)
	copy_to_share()
	print("Copied")
	print("Creating link in /usr/bin")
	create_link()
	print("Created")
	print("Installation finished")


if __name__ == "__main__":
	main()