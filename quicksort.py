def partition(arr, lo, hi) -> int:
    pivot = arr[hi]
    idx = lo - 1

    # do we weaksort
    for i in range(lo,hi):
        if arr[i] <= pivot:
            idx += 1
            tmp = arr[i]
            arr[i] = arr[idx]
            arr[idx] = tmp
    idx +=1
    arr[hi] = arr[idx]
    arr[idx] = pivot

    return idx


def quicksort(arr, lo, hi):
    if lo >= hi:
        return
    
    pivot_idx = partition(arr, lo, hi)
    quicksort(arr, lo, pivot_idx-1)
    quicksort(arr, pivot_idx + 1, hi)

if __name__ == "__main__":
    arr = [7,3,2,4,5]
    quicksort(arr, 0, len(arr)-1)
    sorted = [2,3,4,5,7]

    assert arr == sorted