#import random
#import string

#def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
 #   char_pool = ''
 #   if use_upper:
 #       char_pool += string.ascii_uppercase
  #  if use_lower:
   #     char_pool += string.ascii_lowercase
   # if use_digits:
    #    char_pool += string.digits
    #if use_symbols:
  #      char_pool += string.punctuation
#
 #   if not char_pool:
  #      return "Error: No character types selected."
#
 #   return ''.join(random.choice(char_pool) for _ in range(length))

#while True:
 #   print("\n--- Password Generator ---")
  #  try:
   #     length = int(input("Enter password length: "))
    #    if length <= 0:
     #       print("Length must be positive.")
      #      continue
    #except ValueError:
     #   print("Please enter a valid number.")
      #  continue

    #use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    #use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    #use_digits = input("Include digits? (y/n): ").lower() == 'y'
    #use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    #password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    #print("🔐 Your Password:", password)

    #again = input("Generate another? (y/n): ").lower()
   # if again != 'y':
    #    break
