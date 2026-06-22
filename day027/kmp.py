def build_lps(pattern):
    n = len(pattern)
    lps = [0] * n
    length = 0  # length of previous longest prefix suffix
    i = 1
    
    while i < n:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # Pichli matched length pe fallback karo
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    return lps


def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = build_lps(pattern)
    
    i = j = 0  # i = text index, j = pattern index
    positions = []
    
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                positions.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return positions


print(kmp_search("ababcababcabc", "abc"))  # [2, 7, 10]