def Fs(n: int) -> list[int]:
    if n < 1:
        raise ValueError("`n` is smaller than 1")

    if n <= 2:
        return [1] * n

    fst = 1
    snd = 1
    def f() -> int:
        nonlocal fst, snd
        fst, snd = snd, fst + snd
        return snd
    return [1, 1] + [f() for _ in range(3, n+1)]


n = int(input("> "))
fibonacci = Fs(n)
print("fibonacci:", ', '.join(map(str, fibonacci)))
print("fibonacci (even):", ', '.join(map(str, filter(lambda x: not x % 2, fibonacci))))
print("fibonacci (odd):", ', '.join(map(str, filter(lambda x: x % 2, fibonacci))))
