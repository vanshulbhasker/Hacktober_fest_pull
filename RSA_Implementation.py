print("Shubham Mittal . 36814802717 . 7C5")

import random

# Max length of prime numbers
max_PrimLength = 10000

# Calculates the gcd of two integers
def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

# Calculates the modular inverse from e and phi
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Checks if a number is a prime
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

# Generates Random Prime Number
def generateRandomPrime():
    flag=0
    while(!flag):
        randomPrime = random.randint(0,max_PrimLength)
        if is_prime(randomPrime):
            return randomPrime

# Generates key pairs [Public key pair(e,n)] and [Private key pair(d,n)]
def generate_keyPairs():
    p = generateRandomPrime()
    q = generateRandomPrime()
    
    # n = p*q
    n = p*q
    print("n = ",n)

    # phi(n) = phi(p)*phi(q)
    phi = (p-1) * (q-1) 
    print("phi = ",phi)
    
    # choose 'e' Co-prime to n and 1 > e > phi
    e = random.randint(1, phi)
    g = gcd(e,phi)
    while g != 1:
        e = random.randint(1, phi)
        g = gcd(e, phi)
        
    print("e = ",e)
    
    # d = modular inverse of e and phi
    d = egcd(e, phi)[1]
    
    # make sure d is positive
    d = d % phi
    if(d < 0):
        d += phi

    print("d = ",d)
        
    return ((e,n),(d,n))

def encrypt(text,public_key):
    key,n = public_key

    # Encrypt every chracter of the string and store result into a List
    encryptedText = [pow(ord(char),key,n) for char in text]

    # return encrypted List
    return encryptedText

def decrypt(encryptedText,private_key):
    try:
        key,n = private_key

        # Decrypt every chracter of the encrypted message and store result into a List
        text = [chr(pow(char,key,n)) for char in encryptedText]

        # Return List as Joined single Text
        return "".join(text)
    except TypeError as e:
        print(e)

# Ask user to Enter Message
inputStr = str(input("Enter message to be Encrypted: "))

# Generate Public Key and Private key Pairs and store them
public_key,private_key = generate_keyPairs() 
print("Public key pair (e,n): ",public_key)
print("Private key pair (d,n): ",private_key)

# Encrypt message with public key pair
encryptedText = encrypt(inputStr,public_key)
print("encrypted  = ",encryptedText)

# Decrypt encrypted message with private key pair
decryptedText = decrypt(encryptedText, private_key)
print("decrypted = ",decryptedText)
