acronyms = {'LOL': 'laugh out loud',
            'IDK': "I don't know",
            'TBH': "To be honest"}

try:
    def acronyms['LOL']
    print("The definition of ", acronym, ' is ', definition)
except:
    print("The Key does not exist")

print("the program keeps going")