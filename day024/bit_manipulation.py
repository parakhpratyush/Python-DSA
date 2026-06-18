def bit_tricks():
    # Basic operations
    print("5 & 3 =", 5 & 3)    # 1
    print("5 | 3 =", 5 | 3)    # 7
    print("5 ^ 3 =", 5 ^ 3)    # 6
    print("5 << 1 =", 5 << 1)  # 10
    print("5 >> 1 =", 5 >> 1)  # 2
    
    # Even/odd check
    for n in [4, 7, 12, 9]:
        print(f"{n} is {'even' if n & 1 == 0 else 'odd'}")
    
    # Power of 2 check
    for n in [1, 2, 3, 4, 8, 16, 15]:
        print(f"{n} power of 2: {n > 0 and (n & (n-1)) == 0}")
    
    # Count set bits (Brian Kernighan's algorithm)
    def count_bits(n):
        count = 0
        while n:
            # n & (n-1) removes the rightmost set bit
            # Kyun? n=1100, n-1=1011, AND=1000 — rightmost 1 hata diya
            n &= (n - 1)
            count += 1
        return count
    
    print("Bits in 13 (1101):", count_bits(13))  # 3
    print("Bits in 7  (0111):", count_bits(7))   # 3

bit_tricks()