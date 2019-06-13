from decimal import Decimal
import fileinput
import sys

def show_help():
	print ("What parameter would you like to change?: ")
	print ('A. Density')
	print ('B. Power Law "fac" parameter')
	print ('C. Power Law "tnat" parameter')
	print ('D. Power Law "expo" parameter')
	print ('E. Mass Flow Rate')
	print("Press `q` to exit")

def functionality_kapra(thing,A):
	print (thing + " to search for:")
	textToSearch = input( "> " )
	textToSearch = float(textToSearch)
	textToSearch = '%.7E' % Decimal(textToSearch)

	print (thing + " to replace it with:")
	textToReplace = input( "> " )
	textToReplace = float(textToReplace)
	textToReplace = '%.7E' % Decimal(textToReplace)

	print ("File to perform Search-Replace on:")
	fileToSearch = input( "> " ) or 'polyflow.dat'

	with open(fileToSearch, 'r') as tempFile:
		A_index = 0
		A_Found = False
		lines = tempFile.readlines()
		for index, line in enumerate(lines):
			if A_Found == False and A_index<len(A) and A[A_index] in line:
				A_Found = True
			if A_Found == True and textToSearch in line:
				lines[index] = line.replace(textToSearch, textToReplace)
				print("Match Found")
				A_index +=1
				A_Found = False
		with open(fileToSearch, 'w') as f:
			f.writelines(lines)

def main():
	A = ['BEGIN POWER        1', 'BEGIN PROB1        1', 'BEGIN PROB1        2', 'BEGIN PROB1        9', 'BEGIN PROB1       10']
	B = ['BEGIN BDSVE        1', 'I  3|']
	params = [("a", "Parameter"), ("b", "fac"), ("c", "fnat"), ("d", "expo"), ("e", "Mass flow rate")]
	while True:
		show_help()
		not_found = True
		answer = input()
		answer = answer.casefold()
		for key, value in params:
			if answer == key:
				if answer == 'e' :
					functionality_kapra(value,B)
					not_found = False
				else:
					functionality_kapra(value,A)
					not_found = False

		if answer == 'q':
			print("Sorry to see you go :(")
			break

		if not_found:
			print("Sorry wrong input, try again")

if __name__ == "__main__":
	main()