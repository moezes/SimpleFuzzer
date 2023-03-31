import random


def get_random_bytes(max_length=100, char_start=0, char_range=127):
    payload_len = random.randrange(1, max_length + 1)
    payload = ""
    for i in range(payload_len):
        payload += chr(random.randrange(char_start, char_start + char_range))
    return payload


def main():
    payload = get_random_bytes()
    print(payload)


if __name__ == "__main__":
    main()
