import requests
import random
character_id = random.randint(1, 100)
url = f"https://anapioficeandfire.com/api/characters/{character_id}"
response = requests.get(url)
data = response.json()
character = {
    "Ім'я": data.get("name", "Невідомо"),
    "Стать": data.get("gender", "Невідомо"),
    "Культура": data.get("culture", "Невідомо")
}

print("Згенероване ID: {character_id}")
print("Інформація про персонажа:")
for key, value in character.items():
    print(f"{key}: {value}")