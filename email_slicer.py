email = input('what is your email address? ').strip()

username = email[:email.index('@')]

domain = email[email.index('@') + 1:]

output = "your username is {} and your domain is {}".format(username, domain)

print(output)