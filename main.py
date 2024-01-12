import requests

# We are establishing the needed information for the api
# The scryfall API endpoint I am using in this example requires a minimum of 2 parameters, Set Code and Collector Number. I have Language code so you can look at japanese cards from Strixhaven too.
set_code         = 'cn2'    # Required
collector_number = '70'     # Required
language_code    = 'en'     # Optional

# Using the variables above, we esablish a connection to the API. Link provided in DM to show what our response is in browser; pretty printed.
response = requests.get(f'https://api.scryfall.com/cards/{set_code}/{collector_number}/{language_code}')
json_obj = response.json()

# JSON files are formatted just like dictionaries in python so python has a very easy time iterating through it.
# with json_obj being all the data on the card we want, we can print all the data we want, anywhere we want. xlsx, txt, json, to database, or even just the console (What I'll be doing in the example).
# We know what to put in the square brakets just by looking at what is responsed to us. The link to the json reply is exactly what we are looking through in "json_obj."

card_name    = json_obj['name'] # So name will give us "Selvala, Heart of the Wilds"
set_name     = json_obj['set_name']
release_date = json_obj['released_at']
large_img    = json_obj['image_uris']['large'] # the image_uris is a nested dictionary so we need to tell it the next step too. Otherwise, it would give us the entire dictionary.
cmc          = json_obj['mana_cost']
oracle       = json_obj['oracle_text']

normal_price = json_obj['prices']['usd']
foil_price   = json_obj['prices']['usd_foil']

# I do some fancy stuff in the print statements to underline, ignore the gibrish.
print(f'The card we looked for is \x1B[4m {card_name} \x1B[0m from \x1B[4m {set_name}. \x1B[0m It was released on \x1B[4m {release_date} \x1B[0m and now goes for \x1B[4m {normal_price} \x1B[0m normal, or \x1B[4m {foil_price} \x1B[0m foiled.')
print(f'The CMC of the card is {cmc}, and this is what the card does: \n   - {oracle} \n') # \n is a line break. It has to be used within the quotes of a print statement
print(f"If you'd like to see what the card looks like, please go to the link below: \n    {large_img}") # in Python single quotes ('') and double quotes ("") are usually interchangeable. I had a contraction in this sentence so I had to swap to ""