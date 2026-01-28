## packages, libraries, framework 

import pandas as pd


data = {
    "names": ["sam", "jam", "ram"],
    "numbers": [121221,12121212,34343]
}

dataframe = pd.DataFrame(data)

print(dataframe)
print(type(dataframe))