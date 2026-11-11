def count_letters(word) -> tuple[int, int]:
    return (lt := sum(1 for x in word if x.isalpha()), len(word) - lt)


def count_letters_extended(word: str) -> tuple[int, int]:
    letters_count = 0
    for x in word:
        if x.isalpha():
            letters_count = letters_count + 1
    return letters_count, len(word) - letters_count
