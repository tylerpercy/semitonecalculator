from math import log

def get_semitones(base, target):
    numerator = 12 * log(target/base)
    denominator = log(2)

    return numerator / denominator
    
print("Enter base BPM: ", end= "")
base = int(input())
print("Enter target BPM: ", end= "")
target = int(input())

ans = get_semitones(base, target)
cents = ans * 100

print(f"Adjust by {ans:.2f} semitones ({cents:.0f} cents) to go from {base} BPM to {target} BPM.")

