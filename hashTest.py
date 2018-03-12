from hashlib import sha256

x = 5
y = 0 # We dont know the value of Y yet

while sha256(f'{x * y }'.encode()).hexdigest()[-1] != "0":
    y += 1

print(f'The Solution is y = {y}')