def binary_search(array, k, n):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == k:
            return mid
        elif array[mid] < k:
            #keep the right half and throw out the left half
            start = mid + 1
        elif array[mid] > k:
            #keep the left half and throw out the right
            end = mid - 1

    return -1 #fail flag

def main():
    array = [1,3,5,6,7,8]
    k = 90
    size = len(array)
    result = binary_search(array, k, size)

    if result < 0:
        print("not found")
    else:
        print(f"The target {k} is at index {result}")

main()