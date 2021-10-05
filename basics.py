
################ FIRST CODE: #############################



person = {
    'firstName': 'bryan',
    'lastName': 'smith',
    'city': 'San Francisco',
    'age': '19',

}

print(person['firstName'])
print(person['lastName'])
print(person['city'])
print(person['age'])

for name, key in person.items():
    print(f"\n{name}: \n{key}")


################ SECOND CODE: #############################

favorite_numbers = {
    'bryan': '19',
    'John': '12',
    'Johns': '54',
    'oscar': '1',
    'bruce': '23',
    'marta': '24',

}

print(f"bryan's favorite number is {favorite_numbers['bryan']}")
print(f"John's favorite number is {favorite_numbers['John']}")
print(f"Johns favorite number is {favorite_numbers['oscar']}")
print(f"oscar favorite number is {favorite_numbers['Johns']}")
print(f"bruce favorite number is {favorite_numbers['bruce']}")

for key, value in favorite_numbers.items():
    print(f"{key}  favorite number is {value}")


################ SECOND CODE: #############################

Glossary = {
    'forloops': 'loop thru a variant, constant, or values',
    'if-stat': 'run the following command if its true or false',
    'list': 'store values in the database',
    'dict': 'store values in the database with a given key',
    'variables': 'store a value in a variable to use it later',
}

key = list(Glossary)
print('\n\n')
print(f" {key[0].title()}: {Glossary['forloops']}\n", f"{key[1].title()}: {Glossary['if-stat']}\n", f"{key[2].title()}: {Glossary['list']}\n", f"{key[3].title()}: {Glossary['dict']}\n", f"{key[4].title()}: {Glossary['variables']}")
print ("\n")

for key, value in Glossary.items():
    print(f"{key.title()}: {value}")


################ SECOND CODE: #############################

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print(f"\nkey: {key}")
    print(f"\nvalue: {value}")


 ################ SECOND CODE: #############################

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for names in favorite_language.keys():
    print(names.title())

 ################ SECOND CODE: #############################

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'erin': 'python',
    }

friends = ['phil', 'sarah', 'erin']

if 'erin' not in favorite_language.keys():
        print("erin join us")
else:
    print('good job erin')
    
for name in favorite_language.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()}, i see you love {language}")
    


################ SECOND CODE: #############################
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for names in sorted(favorite_language.keys()):
    print(f"{names.title()}, thank you for taking the poll") 





################ SECOND CODE: #############################

rivers = {
    'The Nile': 'runs through Egypt',
    'Amazon': 'runs through Colombia',
    'Mississippi': 'runs through Mississippi',
}

for key, value in rivers.items():
    print(f"{key} {value}")




################ SECOND CODE: #############################rivers = {
rivers = {
    'The Nile': 'runs through Egypt' ' egypt',
    'Amazon': 'runs through Colombia' ' colombia',
    'Mississippi': 'runs through Mississippi'  ' mississippi',
}

for key, value in rivers.items():
    print(value)


print("\n")

 ################ SECOND CODE: #############################


favorite_language = {
    'jen': ['python', 'java'],
    'sarah': ['c'],
    'edward': ['ruby'],
    'phil': ['python'],
    }

people = {
    'erin': 'python',
    'philips': 'c',
    'edward': 'ruby',
    'jen': 'python',
}

for name,languages in favorite_language.items():
    print(f"\n{name.title()}'s favorite language are: ")

    for language in languages:
        print(f"\t{language.title()}")

for peoples in people:
    if peoples not in favorite_language:
        print(f"\tyou should take the poll {peoples}")

for favorite in favorite_language:
    
        print(f"\nthanks for taking the poll {favorite}")
print("\n")
 ################ SECOND CODE: #############################

alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'red', 'points': '10'}
alien_2 = {'color': 'yellow', 'points': '15'}

alien = [alien_0, alien_1, alien_2]

for aliens in alien:
    print(aliens)



print("\n")
 ################ SECOND CODE: #############################

#empty list
aliens = []
 # Make 30 aliens from

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': '5'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#show first 5 aliens

for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens we created
print(f"total aliens = {len(aliens)}")

print('\n')
 ################ SECOND CODE: #############################

# Store info about a pizza being ordered

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Sumarize the order.
print(f"You ordered {pizza['crust']} - crust pizza with the following toppings: ")

for topping in pizza['toppings']:
    print(f"\t{topping}")
print('\n')
 ################ SECOND CODE: #############################

favorite_language = {
    'jen': ['python', 'java'],
    'sarah': ['c', 'swift', 'c+'],
    'edward': 'ruby',
    'phil': 'python',
    }

for names, languages in favorite_language.items():
    print(f"{names.title()}'s favorite languages are: ")
    for language in languages:
        print(f"{language.title()}")

print('\n')
 ################ SECOND CODE: #############################

favorite_language = {
    'jen': ['python', 'java'],
    'sarah': ['c', 'swift', 'c+'],
    'edward': ['ruby'],
    'phil': ['python'],
    }

for names, languages in favorite_language.items():
    if len(languages) == 2:
        print(f"\n{names.title()} has 2 favorite languages!!")
        for language in languages:
            print(f"\t{language} ")
    if len(languages) == 3:
        print(f"\n{names.title()} has 3 favorite languages!!")
        for language in languages:
            print(f"\t{language} ")
    if len(languages) == 1:
        print(f"{names.title()} only one language is: ")
        for language in languages:
            print(f"\t{language} ")

print('\n')
 ################ SECOND CODE: #############################

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'located': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'located': 'paris',
    }
}


for username, user_info in users.items():
    print(f"\n username: {username}")
    fullName = (f"{user_info['first']} {user_info['last']}")
    location = (f"{user_info['located']}")
    print(f"\t Full Name: {fullName.title()}")
    print(f"\tLocation: {location.title()}")
print('\n')
 ################ SECOND CODE: #############################

person = {
    'firstName': 'bryan',
    'lastName': 'sqs',
    'city': 'San Francisco',
    'age': '19',
}

person2 = {
    'firstName': 'marta',
    'lastName': 'smith',
    'city': 'San Francisco',
    'age': '20',
}

person3 = {
    'firstName': 'chris',
    'lastName': 'irwin',
    'city': 'los angeles',
    'age': '21',
}

people = [person, person2, person3]


for person in people:
    print(f"\n{person['firstName']} {person['lastName']}, {person['city']}, {person['age']}\n")
print('\n')
 ################ SECOND CODE: #############################

pet1 = {
    'kind': 'dog',
    'owner': 'bryan',
    'name pet': 'perro',
    }

pet2 = {
    'kind': 'cat',
    'owner': 'marta',
    'name pet': 'gato',
    }
pet3 = {
    'kind': 'wolf',
    'owner': 'chris',
    'name pet': 'lobo',
    }
pet4 = {
    'kind': 'parrot',
    'owner': 'james',
    'name pet': 'loro',
    }
pet5 = {
    'kind': 'monkey',
    'owner': 'manuel',
    'name pet': 'mono'
    }

pets = [pet1, pet2, pet3, pet4, pet5]

for pet in pets:
    pet_info = (f" kind: {pet['kind']}\n Owner: {pet['owner']}\n Name pet: {pet['name pet']}\n")
    print(pet_info) 
print('\n')   
 ################ SECOND CODE: #############################

favorite_places = {
    'bryan' : ['georgia', 'germany', 'new york', 'japan'],
    'marta': ['switzerland', 'germany', 'england'],
    'chris' : ['america', 'germany','russia'],

}

for favorite, places in favorite_places.items():
    print(f"\n{favorite.title()} favorite places are: ")
    for place in places:
        print("\t" + place.title())

print('\n')
 ################ SECOND CODE: #############################
favorite_numbers = {
    'bryan': ['19', '20', '21', '22', '23', '24'],
    'John': ['12','13','14','15', '50'],
    'Johns': ['54', '55', '56', '34'],
    'oscar': ['1', '2', '3', '4', '4'],
    'bruce': ['23', '24', '25', '57'],
    'marta': ['24', '25', '26', '98'],
}

for numbers, values in favorite_numbers.items():
    print(f"{numbers} favorite numbers are")
    for value in values:
        print(value)

print('\n')
 ################ SECOND CODE: #############################

cities = {
    'tucson': {
        'locations': 'Arizona',
        'population': 'More than a million',
        'fact': 'Desert of sonora',
    }, 

    'Atlanta ': {
        'locations': 'Georgia',
        'population': 'More than a million',
        'fact': 'city of peaches'
    },
    'Washington DC' :{
        'locations': 'washington',
        'population': 'More than a million',
        'fact': 'capital of united states of America',
    }

}

for city, stat in cities.items():
    print(f"\nCity: {city.upper()}")
    best = (f" State: {stat['locations']}\n Population: {stat['population']}\n Quick fact: {stat['fact']}")
    print(best)


print("\n")
 ################ SECOND CODE: #############################

new_usernames = ['bryan', 'random', 'lmao', 'john']



current_usernames = {
    'admin':{
        'password': 'admin',
        'master key': 'admin1243',
        'secret': '1243',
    },
    'bryan':{
        'password': 'bryan',
        'master key': 'bryan1243',
        'secret': '1243',
    },
    'john':{
        'password': 'john',
        'master key': 'john1243',
        'secret': '1243',
    },
    'james':{
        'password': 'james',
        'master key': 'james',
        'secret': 'james1243',
    },
    'jason':{
        'password': 'jason',
        'master key': 'jason1243',
        'secret': '1243',
    },
}

for name, key in current_usernames.items():
    if current_usernames:
        for current_username in current_usernames:
            if current_username == 'admin':
                print('\n\nHello admin, would you like to see a status report?\n\n')
            elif current_username:
                print(f' welcome back {current_username}')
        for key in current_usernames:
            password = str(input('password'))
            password1 = (f"{key}")
            if password == password1:
                print('correct')
            if password == '/end':
                break
            else:
                print('try again bro')
    for username in new_usernames:
        if username in current_usernames:
            print(f'"{username}" its already in use, try something else ')
        elif username:
            print(f'hey welcome {username}!!! hope you like here')

    else:
        break
print('\n\n')
 ################ SECOND CODE: #############################

prompt = "\n Tell me something and I will repeat it back to you: "
prompt += "\n Enter 'quit' to end the program "

message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)

 ################ SECOND CODE: #############################

 ################ SECOND CODE: #############################

 ################ SECOND CODE: #############################


 ################ SECOND CODE: #############################
