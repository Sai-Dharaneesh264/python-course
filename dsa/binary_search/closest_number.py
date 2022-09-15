A1 = [1, 2, 4, 5, 6, 6, 8, 9]
A2 = [2, 5, 6, 7, 8, 8, 9]



def closest_number(a, target):
    sizeOfInput = len(a)
    l = 0
    r = sizeOfInput

    while l < r:
        mid = (l + r) // 2
        if (a[mid] == target):
            return True
        if (a[mid] > target):
            r = mid
        elif (a[mid] <= target):
            l = mid + 1
        

def binary_search_recursive(a, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(a, target, low, mid)
        else:
            return binary_search_recursive(a, target, mid + 1, high)


def closest_num(A, target):

    min_diff = min_diff_left = min_diff_right = float("inf")
    low = 0
    high = len(A) - 1
    closest_num = None
    print('min_diff:', min_diff)
    if len(A) == 0:
        return None
    
    if len(A) == 1:
        return A[0]
    
    while low <= high:
        mid = (low + high) // 2
        if mid + 1 < len(A):
            min_diff_right = abs(A[mid + 1] - target)
        if mid > 0:
            min_diff_left = abs(A[mid - 1] - target)
        

        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = A[mid - 1]
        
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = A[mid + 1]
        

        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
            if high < 0:
                return A[mid]
        else:
            return A[mid]
    return closest_num


print(closest_num(A1, 11))
print(closest_num(A2, 4))