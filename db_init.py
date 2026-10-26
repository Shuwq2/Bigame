from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.BlackClover
collection = db.monsters

collection.drop()

collection.insert_many([
  {
    "nom": "Dante Zogratis",
    "HP": 180,
    "defense": 130,
    "attaque": 140
  },
  {
    "nom": "Vanica Zogratis",
    "HP": 150,
    "defense": 100,
    "attaque": 125
  },
  {
    "nom": "Zenon Zogratis",
    "HP": 170,
    "defense": 140,
    "attaque": 130
  },
  {
    "nom": "Lucius Zogratis",
    "HP": 200,
    "defense": 150,
    "attaque": 160
  },
  {
    "nom": "Zagred",
    "HP": 175,
    "defense": 120,
    "attaque": 145
  },
  {
    "nom": "Vetto",
    "HP": 155,
    "defense": 115,
    "attaque": 120
  },
  {
    "nom": "Fana",
    "HP": 130,
    "defense": 90,
    "attaque": 115
  },
  {
    "nom": "Rhya",
    "HP": 140,
    "defense": 100,
    "attaque": 110
  },
  {
    "nom": "Patolli",
    "HP": 145,
    "defense": 95,
    "attaque": 125
  },
  {
    "nom": "Megicula",
    "HP": 190,
    "defense": 145,
    "attaque": 155
  }
]
)

collection = db.heros

collection.drop()

collection.insert_many([
  {
    "nom": "Asta",
    "HP": 120,
    "defense": 85,
    "attaque": 100
  },
  {
    "nom": "Yuno",
    "HP": 110,
    "defense": 75,
    "attaque": 95
  },
  {
    "nom": "Noelle Silva",
    "HP": 100,
    "defense": 90,
    "attaque": 85
  },
  {
    "nom": "Yami Sukehiro",
    "HP": 150,
    "defense": 100,
    "attaque": 120
  },
  {
    "nom": "Luck Voltia",
    "HP": 95,
    "defense": 65,
    "attaque": 105
  },
  {
    "nom": "Magna Swing",
    "HP": 105,
    "defense": 80,
    "attaque": 85
  },
  {
    "nom": "Mereoleona Vermillion",
    "HP": 160,
    "defense": 110,
    "attaque": 130
  },
  {
    "nom": "Fuegoleon Vermillion",
    "HP": 140,
    "defense": 100,
    "attaque": 110
  },
  {
    "nom": "Julius Novachrono",
    "HP": 145,
    "defense": 95,
    "attaque": 125
  },
  {
    "nom": "Mimosa Vermillion",
    "HP": 90,
    "defense": 75,
    "attaque": 65
  }
]
)