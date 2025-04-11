# evaluate.py
print("Step 3: Evaluating model...")
with open("model.txt", "r") as f:
    model = f.read()
print(f"Evaluation result: {model} is awesome!")
