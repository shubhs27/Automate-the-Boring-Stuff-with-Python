import re

message= "Hey, my phone is 455-555-1000 and not 415-555-9999 in the us format"

phoneNumRegex= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')    # to create regex object
mo=phoneNumRegex.search(message)
print(mo)
print()
print(mo.group())
print()
print(phoneNumRegex.findall(message))
print()

#################################################################################

# use () to make groups in the pattern, if we have an actual () in the message, use \(
phoneNumRegex= re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')    # to create regex object
mo=phoneNumRegex.search(message)
print(mo.group(1))
print(mo.group(2))
print()

batRegex= re.compile(r'Bat(man|mobile|copter)') # use | to match one of many possible groups
mo= batRegex.search('I am Batman')
print(mo.group())   # if the search doesn't find a matching value, it returns None value (printing it will cause error)
print()

#################################################################################

batRegex= re.compile(r'Bat(wo)?man')    # ? means it occurs 0 or 1 times
print(batRegex.search('I am Batman'))
print(batRegex.search('I am Batwoman'))
print()

batRegex= re.compile(r'Bat(wo)*man')    # * means it occurs 0 or more times
print(batRegex.search('I am Batwowowoman'))
print()

batRegex= re.compile(r'Bat(wo)*man')    # + means it occurs 1 or more times
print(batRegex.search('I am Batwoman'))
print()

batRegex= re.compile(r'Bat(wo){2}man')    # {3} means exactly 3 times
print(batRegex.search('I am Batwowoman'))
print()

batRegex= re.compile(r'Bat(wo){2,5}man')    # {3,7} means atleast 3 & atmost 7 times
print(batRegex.search('I am Batwowowowoman'))
print()

digitRegex= re.compile(r'(\d){3,5}')     # greedy (longest) matches in ambiguous situations
print(digitRegex.search('123456789'))
digitRegex= re.compile(r'(\d){3,5}?')    # add ? for non-greedy matches
print(digitRegex.search('123456789'))
print()

#################################################################################

phoneNumRegex= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall(message))       # returns list of strings if there are 0 or 1 group

phoneNumRegex= re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneNumRegex.findall(message))       # returns list of tuples containing strings if there are more than 2 groups
print()

# \d - any digit,                   \D - not any digit
# \w - any letter/digit/_,          \W - not any \w
# \s - any space/tab/newline,       \S - not any \s

vowelRegex= re.compile(r'[aeiou]')     # can also write a range (r'a-z')
print(vowelRegex.findall('Robocop Eats food.'))

vowelRegex= re.compile(r'[^aeiouAEIOU]')     # ^ means negative character class
print(vowelRegex.findall('Robocop Eats food.'))

vowelRegex= re.compile(r'[aeiou]', re.I)     # can also write a range (r'a-z')
print(vowelRegex.findall('Robocop Eats food.'))
print()

#################################################################################

beginRegex= re.compile(r'^Hello')           # ^ means should start with
print(beginRegex.search('Hello world'))
print(beginRegex.search('Yo, Hello world'))

endRegex= re.compile(r'world$')             # $ means should end with
print(endRegex.search('Hello world'))

digitRegex= re.compile(r'^\d+$')            # should start and end with
print(digitRegex.search('123456789'))
print()

atRegex= re.compile(r'.at')                 # . means anything except newline
print(atRegex.findall('The cat is in the flat mat'))    # flat doesn't match

nameRegex= re.compile(r'First Name: (.*) Last Name: (.*)')              # .* is greedy, .*? is non-greedy
print(nameRegex.findall('First Name: Shubhanan Last Name: Sharma'))
print()

dotStarRegex= re.compile(r'.*')
print(dotStarRegex.search('I am Batman.\nThe hope of mankind.'))
dotStarRegex= re.compile(r'.*', re.DOTALL)
print(dotStarRegex.search('I am Batman.\nThe hope of mankind.'))
print()

#################################################################################

secret= 'Agent Michael gave the documents to Agent Dwight.'
namesRegex= re.compile(r'Agent \w+')
print(namesRegex.findall(secret))
print(namesRegex.sub('REDACTED', secret))
print()

namesRegex= re.compile(r'Agent (\w)\w*')
print(namesRegex.findall(secret))
print(namesRegex.sub(r'Agent \1*****', secret))
print()

phoneNumRegex= re.compile(r'''
(?:
\d\d\d-         # area code (without parens, with dash)
|               # or
\(\d\d\d\)\s?   # area code with parens and no dash
)
\d\d\d          # first 3 digits
-               # second dash
\d\d\d\d        # last 4 digits
#\sx\d{2,4}       extension, like x1234
''', re. VERBOSE)        # in verbose whitespace doesn't reflect the actual pattern
print(phoneNumRegex.findall(message))
print()