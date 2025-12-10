import re

text = "Contact me at sohail@email.com or call 987-654-3210./
My other email is backup@work.com"
emails = re.findall(r'\S+@\S+', text)  # Finds all emails
phones = re.findall(r'\d{3}[-.]\d{3}[-.]\d{4}', text)  # Finds US-style phones

print("Emails:", emails)
print("Phones:", phones)
