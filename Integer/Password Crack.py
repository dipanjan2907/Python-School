import time
p = input("Enter Password: ")
c = 0
print("Cracking Password...")
l1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:,.<>?`~"
p1 = ""
start_time = time.perf_counter()
for char in p:
    for candidate in l1:
        c += 1
        if char == candidate:
            p1 += candidate
            break
end_time = time.perf_counter()
print(f"Password Cracked: {p1}  [Attempts: {c}]")
print(f"Time Taken: {end_time - start_time:.6f} seconds")
