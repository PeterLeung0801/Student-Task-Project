from heap import MaxHeap

def heap_sort(arr):
    heap = MaxHeap()

    for num in arr:
        heap.insert(num)

    sorted_list = []

    while len(heap.heap) > 0:
        sorted_list.append(heap.extract_max())

    return sorted_list[::-1]

if __name__ == "__main__":
    data = [4, 10, 3, 5, 1]
    print("Original:", data)
    print("Sorted:", heap_sort(data))