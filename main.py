import string

plain_text = "hello world"
shift = 7

# Define the alphabet for lowercase and uppercase letters
alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase

# Create the shifted versions of the alphabets
shifted_lower = alphabet_lower[shift:] + alphabet_lower[:shift]
shifted_upper = alphabet_upper[shift:] + alphabet_upper[:shift]

# Create a translation table for both lowercase and uppercase letters
table = str.maketrans(alphabet_lower + alphabet_upper, shifted_lower + shifted_upper)

# Encrypt the plain text
encrypted = plain_text.translate(table)

print(encrypted)
