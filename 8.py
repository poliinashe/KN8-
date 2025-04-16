import requests
import random
character_id = random.randint(1, 100)
url = f"https://anapioficeandfire.com/api/characters/{character_id}"
response = requests.get(url)
data = response.json()
character = {
    "��'�": data.get("name", "�������"),
    "�����": data.get("gender", "�������"),
    "��������": data.get("culture", "�������")
}

print("����������� ID: {character_id}")
print("���������� ��� ���������:")
for key, value in character.items():
    print(f"{key}: {value}")