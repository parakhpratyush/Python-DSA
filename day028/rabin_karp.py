def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    if m > n:
        return []
    
    base = 256
    mod = 10**9 + 7
    
    # Pattern ka hash calculate karo
    pattern_hash = 0
    for char in pattern:
        pattern_hash = (pattern_hash * base + ord(char)) % mod
    
    # Pehli window ka hash
    window_hash = 0
    for char in text[:m]:
        window_hash = (window_hash * base + ord(char)) % mod
    
    # base^(m-1) precompute karo rolling hash ke liye
    h = pow(base, m - 1, mod)
    
    positions = []
    
    for i in range(n - m + 1):
        if window_hash == pattern_hash:
            # Hash match — characters verify karo
            if text[i:i+m] == pattern:
                positions.append(i)
        
        if i < n - m:
            # Rolling hash — purana character hatao, naya add karo
            window_hash = (window_hash - ord(text[i]) * h) * base
            window_hash = (window_hash + ord(text[i + m])) % mod
    
    return positions


print(rabin_karp("ababcababcabc", "abc"))  # [2, 7, 10]