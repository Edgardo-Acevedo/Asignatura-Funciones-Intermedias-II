# Parte Uno / lo primero es pasar los arreglos a diccionarios, los que se puedan.

x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)

# ---- #
dict_students0 = {}
def update_students0(students0):
    for st in range(len(students0)):
        dict_students0.update(students0[st])
        if(dict_students0['last_name'] == 'Jordan'):
            dict_students0['last_name'] = 'Bryan'
            break
        first_name_dict_students0 = dict_students0['first_name']
        last_name_dict_students0 = dict_students0['last_name']
        print(f'first_name - {first_name_dict_students0}, last_name : {last_name_dict_students0}')
        dict_students0.clear
update_students0([
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_ndame' : 'Rosales'}
])


# ---- #
dict_sports_directory = {}
def function_sports_directory(directory):
    dict_sports_directory.update(directory)
    if(directory['soccer'] == ['Messi', 'Ronaldo', 'Rooney']):
        directory['last_name'] = ['Andres', 'Ronaldo', 'Rooney']
    basketball_dict_sports_directory = directory['basketball']
    soccer_dict_sports_directory = directory['soccer']
    print(f'first_name - {basketball_dict_sports_directory}, last_name : {soccer_dict_sports_directory}')
function_sports_directory({
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
})

# ---- #

dict_de_z = {}
def function_of_z(zeta):
    dict_de_z.update(zeta[0])
    if(dict_de_z['y'] == 20):
        dict_de_z['y'] = 30
    key_y = dict_de_z['y']
    key_x = dict_de_z['x']
    print(f'x : {key_x}, y : {key_y}')
function_of_z([ {'x': 10, 'y': 20} ])


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Parte Dos
dict0 = {}
def iterateDictionary(estudiantes):
    for a in range(len(estudiantes)):
        dict0.update(estudiantes[a])        
        first_name_Dict0 = dict0['first_name']
        last_name_Dict0 = dict0['last_name']
        print(f'first_name - {first_name_Dict0}, last_name : {last_name_Dict0} ')
        dict0.clear
iterateDictionary([
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ])


# Parte Tres
    
# tomando a la función anterior vamos a tomar los valores de "first_name" y "last_name" 
dict4 = {}
def iterateDictionary2(students):
    for b in range(len(students)):
        dict4.update(students[b])        
        first_name_Dict4 = dict4['first_name']
        print(f'{first_name_Dict4}')
        dict4.clear
    for c in range(len(students)):
        dict4.update(students[c])        
        last_name_Dict4 = dict4['last_name']
        print(f'{last_name_Dict4}')
        dict4.clear
iterateDictionary2([
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ])
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #


def printInfo(dict_of_dojo):
    for k,v in dict_of_dojo.items():
        l = len(v)
        k = k.upper()
        print(f'{l} {k}')
        for V in v:
            print(V)

printInfo({'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']})

  