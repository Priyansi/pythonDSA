#!python3
import random


def generate_random_prime() -> int:
    LIST_OF_PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                      97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    return random.choice(LIST_OF_PRIMES)


def hash_string(string: str, base: int, prime: int) -> int:
    str_to_num = 0
    size = len(string)
    for i in range(size):
        str_to_num += ord(string[i])*(base**(size-i-1))
    return str_to_num % prime


def append(hash_text_window: int, val: str, base: int, prime: int) -> int:
    return (hash_text_window*base + ord(val)) % prime


def skip(hash_text_window: int, val: str, skip_multiplier: int, base: int, prime: int) -> int:
    return (hash_text_window - ord(val) * skip_multiplier + base*prime) % prime


def rabin_karp(pat: str, text: str, base: int) -> list:
    found_at_indexes = []
    prime = 11
    length_pat = len(pat)

    hash_pat = hash_string(pat, base, prime)
    hash_text_window = hash_string(text[:length_pat], base, prime)
    if hash_pat == hash_text_window:
        if pat == text[0:length_pat]:
            found_at_indexes.append(0)

    curr_start_ch_index = 0
    curr_index = length_pat
    skip_multiplier = (base**(length_pat-1)) % prime

    while curr_index < len(text):
        hash_text_window_skip = skip(
            hash_text_window, text[curr_start_ch_index], skip_multiplier, base, prime)
        hash_text_window = append(
            hash_text_window_skip, text[curr_index], base, prime)

        curr_start_ch_index += 1
        curr_index += 1

        if hash_pat == hash_text_window:
            if pat == text[curr_start_ch_index:curr_index]:
                found_at_indexes.append(curr_start_ch_index)

    return found_at_indexes


if __name__ == "__main__":
    pat = 'Karp'
    text = 'Hello World. I am using Rabin-Karp to find the word Karp.'
    base = 256
    print('Pattern found at {}'.format(rabin_karp(pat, text, base)))
    # Output - Pattern found at [30, 52]
