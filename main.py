clean = []

print("Starting...")
with open("tokens.txt", "r") as f:
    lines = f.read().splitlines()
    for line in lines:
        split = line.split(":")
        clean.append(split[2])
    
with open("output.txt", "w") as f:
    for token in clean:
        f.write(f"{token}\n")

print("Done!")