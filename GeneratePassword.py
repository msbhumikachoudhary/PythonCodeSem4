import random
import string

def generate_password(length, lowercase=True, uppercase=True, digits=True, symbols=True):
  
  char_set = ""
  if lowercase:
    char_set += string.ascii_lowercase
  if uppercase:
    char_set += string.ascii_uppercase
  if digits:
    char_set += string.digits
  if symbols:
    char_set += string.punctuation

  if not char_set:
    raise ValueError("Please choose at least one type of character (lowercase, uppercase, digits, or symbols).")

  password = ''.join(random.sample(char_set, length))
  return password


desired_length = 12
password = generate_password(desired_length)
print(f"Generated password: {password}")
