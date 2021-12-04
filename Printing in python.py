#Printing multiple value
print("Hello, EngSci")

print("Hello" + ", " + "EngSci")

subj = "ECE"
print("Hello" + ", " + subj)

program_rating = 7.9
print(subj, program_rating)

print (subj + " " + str(program_rating))
print(subj, ":", program_rating)

#print("Artscies are "smart"")#this will not work

print("Artscies are 'smart'")
print("Artscies are \"smart\"") #\"smart\" are to tell python to print double quotes and not think of it as code
#similarly, it works for single quote
print('Artscie sare \'smart\'')
#to print backslash \, use double backslash like \\
print("Tea\\Coffee")

#to print multiline strings,
print("""abc
def
ijk""")
#or
print('''abc
def
ijk''')
#or use \n to change line
print("abc\ndef\nijk")

