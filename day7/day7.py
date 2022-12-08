import os

class directory:
	def __init__(self):
		self.size = 0
		self.files = []
		self.name = ""
	def __str__(self):
		strRet = ""
		strRet += "type=directory name="+ self.name + "size=" + str(self.size)
		strRet += "\nfiles in this directory:\n"
		if len(self.files) == 0:
			strRet += ("None")
		else:
			for f in self.files:
				strRet += f.__str__
				strRet += "\n"

		return strRet
		
class file:
	def __init__(self):
		self.size = 0
		self.name = ""

	def __str__(self):
		return (f"type=file name={self.name} size={self.size}")
	def ret(self):
		return (f"type=file name={self.name} size={self.size}")

def main():

	line = [l.strip() for l in open(os.getcwd() + "/example7.txt")]
	root = directory()
	root.name = "/"
	i = 1
	currentDir = root
	checkForFiles = False
	while i < len(line):
		if checkForFiles:
			if "dir" in line[i]:
				# create a new dir and add it to the current directory
				newDir = directory()
				currentDir.parent = newDir
				newDir.name = line[i][4]
				currentDir.files.append(newDir)
				print(f"create new directory: {newDir.name}")
				checkForFiles = False
			else:
				newFile = file()
				newFile.name = line[i][line[i].index(" ")+1]
				newFile.size = int(line[i][:line[i].index(" ")])
				checkForFiles = False
				
									
		if "$ ls" in line[i]:
			checkForFiles = True


		i += 1

	print(root)
	return 0


if __name__ == "__main__":
	main()
