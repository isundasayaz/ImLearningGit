

class stringTests:
    #string = "SundasAyaz!"

    def functionforStrings(self, string):
        for x in range(8):
            print(string[x])
    def TestStringInString(self, string , string1):
        print(string in string1)




string = "!CLASSSundasAyaz"
strint1 = "Sundas"
string2 = "rahulshettyacademy.com"

object1 = stringTests()

object1.functionforStrings(string)
object1.TestStringInString("a" , "b")

string3 = "   blah.blah   "
string4= string3.split(".")
print(string4)
print(string3.strip())
print(string3.lstrip())
print(string3.rstrip())

