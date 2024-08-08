def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return -1

    # Створення таблиці зсувів для символів у шаблоні
    last = {}
    for i in range(m):
        last[pattern[i]] = i

    # Пошук підрядка у тексті
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            s += max(1, j - last.get(text[s + j], -1))
    return -1
