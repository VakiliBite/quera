mykey = input().strip()
key_len = len(mykey)
n = int(input().strip())

guesses = [input().strip() for _ in range(n)]

results = []
game_over = False

for guess in guesses:
    if game_over:
        results.append("Game Over")
        continue
    
    if len(guess) != key_len:
        results.append("Invalid Length")
        continue
    
    if guess == mykey:
        results.append('G' * key_len)
        game_over = True
        continue
    
    used = [False] * key_len
    output = [''] * key_len
    
    for i, ch in enumerate(guess):
        if ch == mykey[i]:
            output[i] = 'G'
            used[i] = True
    
    for i, ch in enumerate(guess):
        if output[i] == 'G':
            continue
        found = False
        for j, target in enumerate(mykey):
            if not used[j] and ch == target:
                found = True
                used[j] = True
                break
        output[i] = 'Y' if found else 'R'
    
    results.append(''.join(output))

print('\n'.join(results))