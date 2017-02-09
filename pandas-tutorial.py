import pandas as pd 
import numpy as np 

some_numbers = pd.Series([1, 2, 3])
some_strings = pd.Series(["cat", "dog", "mouse"])
mixed = pd.Series([1, "cat", 3.0])

print some_numbers
print some_strings
print mixed

df = pd.DataFrame({"animal":some_strings, "score":some_numbers*3})
df