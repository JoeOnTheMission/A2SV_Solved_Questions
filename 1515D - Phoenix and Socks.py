from collections import Counter

t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    socks = list(map(int, input().split()))

    left = Counter(socks[:l])
    right = Counter(socks[l:])

    # Cancel free pairs
    for color in list(left.keys()):
        if color in right:
            m = min(left[color], right[color])
            left[color] -= m
            right[color] -= m
            l -= m
            r -= m

    # Make left the bigger side
    if l < r:
        left, right = right, left
        l, r = r, l

    cost = 0

    diff = l - r  # imbalance

    # Count duplicates
    duplicates = 0
    for color in left:
        duplicates += left[color] // 2

    use = min(duplicates, diff // 2)
    cost += use
    diff -= use * 2

    # Remove used duplicates
    for color in left:
        pairs = left[color] // 2
        take = min(pairs, use)
        left[color] -= take * 2
        use -= take
        if use == 0:
            break

    # Remaining imbalance
    cost += diff // 2

    # Remaining recolors
    remaining = sum(left.values()) + sum(right.values())
    cost += remaining // 2

    print(cost)
