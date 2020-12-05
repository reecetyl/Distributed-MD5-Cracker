import string
import itertools

def generate_strings(length=5):
    # generates list of strings using letters A-Z, a-z of desired length
    chars = string.ascii_letters
    return ["".join(item) for item in itertools.product(chars, repeat=length)]

print("Generating dictionary...")
full_dict = generate_strings()
with open('dictionary.txt', 'w') as filehandle:
    for listitem in full_dict:
        filehandle.write('%s\n' % listitem)

print("done")

