# train.py
print("Step 2: Training model...")
with open("data.txt", "r") as f:
    data = f.read()
print(f"Training on: {data}")
with open("model.txt", "w") as f:
    f.write("trained model")
