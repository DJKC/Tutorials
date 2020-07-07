import re, pyperclip

phoneRegex = re.compile(r'''
# (123)1231234 (123)-123-1234 123-1234 1231234 (123) 123 1234 123 1234
# (\(?\d\d\d\)?)? (-|\s|\.)? \d\d\d (-|\s|\.)? \d\d\d\d (\s*(ext|ex|x)\s*\.?\s*\d{3,5})?
# area code with parentheses
((\d{3} | \(\d{3}\))?

# first separator
(-|\s|\.)?

# 3 digit group
(\d{3})

# second separator
(-|\s|\.)?

# last 4 digits
(\d{4})

# extension
(\s*(ext|ex|x)\s*\.?\s*\d{3,5})?)
''', re.VERBOSE)

emailRegex = re.compile(r'''
# jake101_211.344+dfnksf@gmail.com

# username
[a-z0-9_.+-]+

# at sign
@

# domain name
[a-z0-9-.+]+

# top level domain .net .org .com
[a-z0-9-.]+

#[a-z0-9_.+-]+@[a-zA-Z0-9-.+]+[a-zA-Z0-9-.]+ 

''', re.VERBOSE|re.IGNORECASE)

# Get text from clipboard
#text = pyperclip.paste()
text = '''
        Email: daniel.borses@rcc.edu
        Phone: (951) 222-8862
        Email: kenneth.bowyer@rccd.edu​
        Email: dino.buenviaje@rccd.edu
        Email: patience.essah@rcc.edu
        Email: cynthia.gobatie@rcc.edu
        Office: Quad 141
        Richard T. Livingston, Associate Philosophy Faculty
        Email: richard.livingston@rccd.edu
        Kevin Perry Maroufkhani, Assistant Professor of Philosophy and Humanities
        Email: kevin.maroufkhani@rcc.edu
        Office: Quad 100
        Phone: (951) 222-8321
        Romulus C. Masterson (Chair), Associate Professor of Philosophy (FSA: Humanities and Music)
        Email: romulus.masterson@rcc.edu
        Office: Quad 22-
        HUMANITIES
        Kirsten M. Gerdes, Assistant Professor of Philosophy and Humanities
        Email: kirsten.gerdes@rcc.edu
        Phone: (951) 222-8321
        Email: romulus.masterson@rcc.edu
        Email: thomas.yanni@rccd.edu​


'''

print("Text start:\n", text, "\nText end")

# Get email and phone from pasted text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

print("Email: ", extractedEmail)
print("Phone: ", extractedPhone)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print("Numbers list: ", allPhoneNumbers)

# Copy results to clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
