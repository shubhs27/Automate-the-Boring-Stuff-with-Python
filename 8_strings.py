# strings are immutable
print('Thy name\'s not important')
print(r'Thy name\'s not important')     # raw string
print()

print("""this feature 
is for bitches 
who yap a lot""")
print()

str = "lets learn about strings"
print(str.upper())
print(str)
str= str.upper()
print(str)
print()

print(str.islower())
print('123a'.islower())
print('123'.islower())     # there needs to be atleast 1 lowercase character
print('123a'.isalnum())
print()

print('kitne sample du bhai!'.startswith('kitne'))
print('kitne sample du bhai!'.endswith('!'))
print()

names= ["messi", "suarez", "neymar"]
print("-".join(names))
print(str.split())
print(str.split("A"))
print()

print("That's useful".rjust(20))
print("That's useful".center(20,"*"))
print()


print("      I need space...       ".strip())
print("spamspamspamThat's bullshitspam".strip("amps"))
print()

print("fucker".replace('u','*'))
print()

type="format"
percentage= 100
source="trust me bro"
print(f"this is a %s string, its useful %d%% times, source: %s" % (type, percentage, source))   # method 1
print(f"this is a {type} string, its useful {percentage}% times, source: {source}")             # method 2