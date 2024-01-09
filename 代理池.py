import random

proxies_pool = [
    {"http": "http://127.0.0.1:7890"},
    {"http": "http://127.0.0.1:7891"},
    {"http": "http://127.0.0.1:7892"},
    {"http": "http://127.0.0.1:7893"},
    {"http": "http://127.0.0.1:7894"},
    {"http": "http://127.0.0.1:7895"},
]

proxies = random.choice(proxies_pool)

print(proxies)