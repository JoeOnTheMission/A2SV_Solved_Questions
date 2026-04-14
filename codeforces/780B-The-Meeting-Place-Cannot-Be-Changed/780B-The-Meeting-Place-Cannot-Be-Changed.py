def can(time):
    max_left = float("-inf")
    min_right = float("inf")
    for pos,velocity in zip(x,v):
        left = pos - (velocity * time)
        right = pos + (velocity * time)
        max_left = max(max_left,left)
        min_right = min(min_right,right)
    return max_left <= min_right
low = 0
high = (max(x) - min(x))/min(v)
precision = 10**(-6)
while low <= high:
    mid = (low + high) / 2
    if can(mid):
        high = mid - precision
    else:
        low = mid + precision
print(low)