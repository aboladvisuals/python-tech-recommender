roles= {
    "Data Scientist": ["python", "sql", "machine learning"],
    "Data Analyst": ["sql", "excel", "python"],
    "DevOps Engineer": ["aws", "docker", "kubernetes"],
    "Backend Developer": ["java", "python", "sql"],
    "Frontend Developer": ["javascript", "html", "css"],
}

while True:
    text = input("Type at least three skills, separated by commas:").strip().lower()
    skills= [skill.strip() for skill in text.split(",") if skill.strip()]
    if len(skills) < 3:
        print("Need at least three skills.")
        continue
    break

vocabulary= sorted({skill for role_skills in roles.values()for skill in role_skills})

def vector (chosen):
    return [1 if skill in chosen else 0 for skill in vocabulary]

def cosine (left, right):
    dot = sum(a * b for a, b in zip(left, right))
    left_size = sum(a * a for a in left) ** 0.5
    right_size = sum(b * b for b in right) ** 0.5
    if left_size == 0 or right_size == 0:
        return 0.0
    return dot / (left_size * right_size)

scores = []
user_vector = vector(skills)
for role, role_skills in roles.items():
    score = cosine(user_vector, vector(role_skills))
    scores.append((score, role))

scores.sort(reverse=True)

print("Top 3:")
for score, role in scores[:3]:
    print(f"{role}: {score:.2f}")

