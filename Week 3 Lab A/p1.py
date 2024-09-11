score = float(input("score: "))

if score < 0 or score > 100:
    print("Invalid score!")
else:
    score = int(score)
    x = score // 10 - 6
    letter = 'F'
    if x >= 0:
        letter = "DCBAA"[x]
    print("You letter grade is", letter)
