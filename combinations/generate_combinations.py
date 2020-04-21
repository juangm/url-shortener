import itertools
import json
import string

# Create the string with all possible charactesr according to specs
charset = string.ascii_lowercase + string.digits + string.ascii_uppercase

# Calculate all the combinations and convert to a list
list_combinations = list(itertools.product(charset, repeat=2))

# Write all the combination to a json file for later use it
with open("./combinations/encoding.json", "w", encoding="utf-8") as f:
    json.dump(list_combinations, f, ensure_ascii=False, indent=2)
