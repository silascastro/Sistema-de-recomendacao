__author__ = "SILAS CASTRO DE MENDONCA"
__class__  = "SISTEMAS DE INFORMACAO"

"""
    nesse sistema de recomendação analiso não só a nota do produto 
    mas também o author se um usuário gostou de um livro do George Orwell 
    por exemplo também vai gostar de outros livros do mesmo autor.
"""


users = {
    "Fulano":{
        "A revolução dos Bichos": {
            "rate": 5.0, 
            "author": "George Orwell",
            "genero": "ficção"
        },
        "Homo-Sapiens: Uma Breve história da humanidade": 
        {"rate": 5.0, "author": "Yuval Noah Harari", "genero": "história"},
        "1984": {"rate": 5.0, "author": "George Orwell", "genero": "ficção"},
        "O adversário secreto": {"rate": 4.0, "author": "Agatha Christie", 
        "genero": "romance"},
        "21 lições para o século 21": {"rate": 4.5, "author": "Yuval Noah Harari", 
        "genero": "política"}
    },
    "Ciclano":{
        "A revolução dos Bichos": {"rate": 4.0, "author": "George Orwell", "genero": "ficção"},
        "Do átomo ao buraco negro: Para descomplicar a astronomia": 
        {"rate": 3.0, "author": "Schwarza", "genero": "astronomia"},
        "Senhor das moscas": {"rate": 5.0, "author": "William Golding", "genero": "ficção"},
        "Admiravel Mundo novo": {"rate": 5.0, "author": "Aldous Huxley", "genero": "ficção"},
        "1984": {"rate": 5.0, "author": "George Orwell"}
    },
    "Julia": {
        "A revolução dos Bichos": {"rate": 4.0, "author": "George Orwell", "genero": "ficção"},
        "Do átomo ao buraco negro: Para descomplicar a astronomia": 
        {"rate": 4.0, "author": "Schwarza", "genero": "astronomia"},
        "Senhor das moscas": {"rate": 5.0, "author": "William Golding", "genero": "ficção"},
        "Admiravel Mundo novo": {"rate": 1.0, "author": "Aldous Huxley", "genero": "ficção"},
        "1984": {"rate": 3.0, "author": "George Orwell", "genero": "ficção"},
    }
}

def manhattan(rating1:dict, rating2: dict):
    distance = 0
    for key,x in rating1.items():
        if key in rating2:
           distance += abs(rating1[key]["rate"] - rating2[key]["rate"])

    return distance   

def computeNearestNeighbor(username, users):
    distances = []
    for user in users:
        if user != username:
            distance = manhattan(users[user], users[username])
            distances.append((distance, user))
    distances.sort()
    return distances

def recommend(username, users: dict): 
    nearest = computeNearestNeighbor(username,users)[0][1]
    recommendations = []
    neighborRatings = users[nearest]
    
    for book in neighborRatings:
        if book not in users[username]:
            recommendations.append((book, neighborRatings[book]))

    return recommendations

def refina():
    pass

result = recommend("Fulano", users)
print(result)