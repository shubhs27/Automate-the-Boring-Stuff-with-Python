import re, pyperclip

# Create a regex for phone numbers
phoneRegex= re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(           
((\d\d\d) | (\(\d\d\d\)))?   # area code (optional)
(\s|-)                  # first separator
\d\d\d                  # first 3 digits
-                       # second separator
\d\d\d\d                # last 4 digits
(((ext(\.)?\s)|x)       # extension word-part (optional)
(\d{2,5}))?             # extension word-part (optional)
)                       
''', re.VERBOSE)


# Create a regex for email
emailRegex= re.compile(r'''
                       
[a-zA-Z0-9_.+]+     # name part
@                   # @ symbol
[a-zA-Z0-9_.+]+     # domain name part  
                                            
''', re.VERBOSE)


# Get the text off the clipboard
text= pyperclip.paste()


# Extract the email/phone from this text
extractedPhone= phoneRegex.findall(text)
extractedEmail= emailRegex.findall(text)

allPhoneNumbers= []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])


# copy the extracted email/phone to clipboard
results= '\n'.join(allPhoneNumbers) + '\n'.join(extractedEmail)
pyperclip.copy(results)