safe_combo = (5, 12, 97)

print("--- 🔒 THE IMMUTABLE SAFE 🔒 ---")
print("There are 3 dials on the safe.")
print("Hints: [Start small] [Quarter] [Half-century]")

val1 = input("Turn dial 1: ")
val2 = input("Turn dial 2: ")
val3 = input("Turn dial 3: ")

user_attempt = (val1, val2, val3)

print("\n...Clicking mechanism...")
print(f"You attempt: {user_attempt}")
print(f"Safe combo: {safe_combo}")

is_open = (safe_combo == user_attempt)

print("*" * 20)
print(f"Did the safe open: {is_open}")
print("*" * 20)