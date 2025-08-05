"""We use binary search on the sorted version of m,
but the final answer requires the original indices (from the unsorted list)."""
# Binary Search on sorted list
def Binary_search(m, target):
    m_len = len(m)
    low = 0
    high = m_len - 1
    while low <= high:
        mid_idx = (high + low) // 2  # ✅ fix: proper mid formula
        if m[mid_idx] == target:
            return mid_idx
        elif m[mid_idx] < target:
            low = mid_idx + 1
        else:
            high = mid_idx - 1
    return -1  # ✅ fix: indentation

# Generate all cost pairs that sum to total_cost
def combanitaions(total_cost):
    Costs_tuple = []  
    for n1 in range(1, 6):
        for n2 in range(1, 6):
            if (n1 + n2) == total_cost:
                Costs_tuple.append((n1, n2))
    return Costs_tuple

# Main function
def flavour_and_costs(m, total_cost):
    Target = combanitaions(total_cost)
    original_indcies_m = m[:]
    m.sort()

    for a, b in Target:
        idx_a = Binary_search(m, a)
        idx_b = Binary_search(m, b)

        if idx_a != -1 and idx_b != -1:
            if a == b:
                first_index = original_indcies_m.index(a)
                second_index = original_indcies_m.index(b, first_index + 1)
                return sorted([first_index + 1, second_index + 1])  # ✅ return 1-based
            else:
                original_idx_a = original_indcies_m.index(a)
                original_idx_b = original_indcies_m.index(b)
                return sorted([original_idx_a + 1, original_idx_b + 1])  # ✅ return 1-based

    return []  # Fallback if no pair found,  in case no matching pair was found.

# Test case
total_cost = 6
m = [1, 2, 7, 5, 3]
print(flavour_and_costs(m, total_cost))  # ✅ Expected output: [1, 4] indecies(1-based) of these numbers (1, 5 ) 1+5 = 6
