N = int(input())
N_list = list(map(int, input().split()))

N_list = [n for n in N_list if n != 1]

def is_prime(num) :
    if num < 2 :
        return False
    for i in range(2, int(num**0.5 +1)):
        if num%i == 0:
            return False
    return True

prime_list = [x for x in N_list if is_prime(x)]

print(len(prime_list))