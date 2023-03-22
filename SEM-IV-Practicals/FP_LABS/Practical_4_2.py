import string

def is_pangram(s):
    # Create a set of all alphabets
    alphabets = set(string.ascii_lowercase)
    
    # Convert the string to lowercase and remove non-alphabetic characters
    s = set(c.lower() for c in s if c.isalpha())
    
    # Return True if the set of alphabets is a subset of the set of alphabetic characters in the string
    return alphabets.issubset(s)

# Example usage
s = "The quick brown fox jumps over the lazy dog"
if is_pangram(s):
    print(f"{s} is a pangram")
else:
    print(f"{s} is not a pangram")
