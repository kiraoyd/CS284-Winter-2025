#n is the size of the array
def linear_search(array, target, n):
    index = 0
    while index < n:
        if array[index] == target:
            return index
        index += 1

    return -1 #fail flag, target not found


def main():
    collection = [5,1,10,2,4]
    target = 2
    n = len(collection)
    result = linear_search(collection, target, n)

    if result < 0:
        print("Not found.")
    else:
        print(f"{target} is located at index {result}")

main()