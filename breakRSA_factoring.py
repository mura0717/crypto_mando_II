n = 629
e = 17

m_array_encrypted = [247, 337, 322, 463, 15, 73, 440, 15, 342, 323, 435]
m_array_decrypted = []

c = m_array_encrypted[0]

def isPrime(num):
    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            return False
    return True

n_factors = []
           
def factor_n(n_given):
    for i in range(1,n_given+1):
        if n_given % i == 0 and isPrime(i):
            n_factors.append(i)
    print("n_factors:", n_factors)

factor_n(n)

p_q_factors = []

def find_p_q(given_n_factors):
    for i in given_n_factors:
        if given_n_factors[i] * given_n_factors[i+1] == n:
            p_q_factors.append(given_n_factors[i])
            p_q_factors.append(given_n_factors[i+1])
            print("p and q are:", p_q_factors)
            return p_q_factors
        else:
            print("No match.") 
            
find_p_q(n_factors)

p = p_q_factors[0]
print("p is:",p)
q = p_q_factors[1]
print("q is", q)

def find_private_key(given_p, given_q):
    phi_n = (given_p - 1) * (given_q - 1)
    private_key = pow(e, -1, phi_n)
    print("d is:", private_key)
    return private_key

d = find_private_key(p,q)

def decrypt(c):
    m = c**d % n
    m = chr(m)
    return m

for c in m_array_encrypted:
    m_array_decrypted.append(decrypt(c))

print("".join(m_array_decrypted))

