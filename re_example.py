import re

# Create a pattern
pattern = re.compile('Hello, (\\w+)!')

# Match the pattern
match = pattern.match('Hello, world!')

# Print the match
print(match.group(1))