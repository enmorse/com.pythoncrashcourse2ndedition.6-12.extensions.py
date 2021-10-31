# Make a dictionary named cities. Use the names
# of three cities as keys in your dictionary. Create
# a dictionary of information about each city and
# include the country that the city is in, its
# approximate population, and one fact about that
# city. The keys for each city's dictionary should
# be something like country, population, and fact.
# Print the name of each city and all of the
# information you have stored about it.

# We're now working with examples that are
# complex enough that they can be extended in any
# number of ways. Use one of the example programs
# from this chapter, and extend it by adding new keys
# and values, changing the context of the program,
# or improving the formatting of the output.

cities = {
    'waterdeep': {
        'world': 'forgotten realms',
        'population': 130000,
        'fact': 'also known as the city of splendors',
    },
    'solace': {
        'world': 'krynn',
        'population': 197016,
        'fact': 'home of the inn of the last home',
    },
    'the shire': {
        'world': 'middle-earth',
        'population': 65000,
        'fact': 'home to bilbo and frodo baggins',
    },
    'solamina, palanthas': {
        'world': 'krynn',
        'population': 32000,
        'fact': 'my first d&d character was a knight of'
                'solamnia',
    },
}

for key, value in cities.items():
    print(f"\n{key.title()}: ")
    print(f"{value}")
