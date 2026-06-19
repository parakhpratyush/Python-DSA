def activity_selection(activities):
    # activities = list of (start, end) tuples
    
    # End time ke hisaab se sort karo
    # Kyun? Jaldi khatam hone wali activity
    # baaki ke liye zyada room deti hai
    activities.sort(key=lambda x: x[1])
    
    selected = []
    
    # Pehli activity hamesha select karo
    # (sabse pehle khatam hone wali)
    last_end = 0
    
    for start, end in activities:
        # Agar current activity ka start time
        # last selected activity ke end time se >= hai
        # No overlap — select karo
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    
    return selected

# Test
activities = [(1,3), (2,5), (3,9), (6,8)]
print("Selected:", activity_selection(activities))
# [(1,3), (6,8)]

activities2 = [(0,6), (1,4), (3,5), (3,8), (4,7), (5,9), (6,10), (8,11)]
print("Selected:", activity_selection(activities2))