def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def check_list(lst):
    """Check the list based on the given conditions."""
    all_prime = all(is_prime(x) for x in lst)
    sum_is_prime = is_prime(sum(lst))
    
    if all_prime:
        return "CORRECT"
    elif not all_prime and sum_is_prime:
        return "CORRECT"
    else:
        return "INCORRECT"
