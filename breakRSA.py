n = 629
e = 17

m_array_encrypted = [247, 337, 322, 463, 15, 73, 440, 15, 342, 323, 435]
m_array_decrypted = []

c = m_array_encrypted[0]


def break_m(equal):
    for i in range(1000):
        test = i**e % n
        if test == equal:
            return i


m = break_m(m_array_encrypted[0])


def isprime(num):
    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            return False
    return True


def find_private_key():
    for d in range(10000):
        m_test = c**d % n
        if m_test == m:
            if isprime(d):
                return d


d = find_private_key()


def decrypt(c):
    m = c**d % n
    m = chr(m)
    return m


for c in m_array_encrypted:
    m_array_decrypted.append(decrypt(c))

print("".join(m_array_decrypted))
