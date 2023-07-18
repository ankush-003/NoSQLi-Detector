import json
import random

# Define the template variations and injection payloads
templates = [
    {"template": '{"username": "<placeholder>", "password": "password"}', "payload": '{"$ne": ""}'},
    {"template": '{"userId": "<placeholder>", "isAdmin": false}', "payload": '{"$gt": 0}'},
    {"template": '{"email": "<placeholder>", "verified": true}', "payload": '{"$regex": ""}'},
    {"template": '{"query": {"$regex": "<placeholder>"}}', "payload": '".*"'}, 
    {"template": '{"$where": "<placeholder>"}', "payload": '1'}
]

# Generate the dataset
dataset = []
for template in templates:
    for i in range(10):  # Generate multiple variations of each template
        placeholder = f"payload{i}"
        generated_template = template["template"].replace("<placeholder>", placeholder)
        generated_payload = template["payload"].replace("<placeholder>", placeholder)
        dataset.append({"template": generated_template, "payload": generated_payload})

# Shuffle the dataset
random.shuffle(dataset)

# Add additional samples to increase diversity
additional_samples = 100
for _ in range(additional_samples):
    template = random.choice(templates)
    placeholder = f"payload{random.randint(100, 999)}"
    generated_template = template["template"].replace("<placeholder>", placeholder)
    generated_payload = template["payload"].replace("<placeholder>", placeholder)
    dataset.append({"template": generated_template, "payload": generated_payload})

# Save the shuffled dataset to a JSON file
with open("nosql_injection_dataset.json", "w") as f:
    json.dump(dataset, f, indent=4)

print("Dataset generated, shuffled, and saved as nosql_injection_dataset.json.")
