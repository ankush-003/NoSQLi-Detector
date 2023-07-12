import random
import json

# List of characters to use for generating payloads
characters = ['"', "'", ';', '=', '{', '}', '(', ')', '[', ']', '$', '*', '|', ':', '^']

# List of example queries and their corresponding labels (1 for malicious, 0 for benign)
queries = [
    ('{"username": "{}"}', 0),
    ('{"username": "{$ne: null}"}', 1),
    ('{"$where": "this.username === \'{}\'"}', 1),
    ('{"username": {"$regex": "^{}"}}', 1),
    ('{"username": {"$ne": "{}"}}', 1),
    ('{"username": {"$gt": "{}"}}', 1),
    ('{"$or": [{"username": "{}"}, {"isAdmin": true}]}', 1),
]

# Number of benign queries to generate
num_benign = 5000

# Number of malicious queries to generate
num_malicious = 5000

# Output file path
output_file = "dataset.json"

# Generate benign queries
benign_samples = []
for _ in range(num_benign):
    query, label = random.choice(queries)
    payload = random.choice(characters).join(query.split('"{}"'))
    benign_samples.append((payload, label))

# Generate malicious queries
malicious_samples = []
for _ in range(num_malicious):
    query, label = random.choice(queries)
    payload = random.choice(characters).join(query.split('"{}"'))
    payload += random.choice(characters)
    malicious_samples.append((payload, label))

# Combine benign and malicious samples
samples = benign_samples + malicious_samples

# Shuffle the samples
random.shuffle(samples)

# Create a list of dictionaries for the dataset
dataset = []
for sample in samples:
    payload, label = sample
    data_point = {"text": payload, "label": label}
    dataset.append(data_point)

# Write dataset to the output file
output_file = "dataset.json"
with open(output_file, 'w') as f:
    json.dump(dataset, f, indent=2)

print(f"Dataset generated and saved to {output_file}")
