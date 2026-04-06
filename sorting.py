def print_step(step, arr):
    print(f"Iterasi {step}: {arr}")

# Bubble Sort
def bubble_sort(arr):
    a = arr.copy()
    step = 1
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            print_step(step, a)
            step += 1
    print("Hasil Bubble:", a)

# Selection Sort
def selection_sort(arr):
    a = arr.copy()
    step = 1
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        print_step(step, a)
        step += 1
    print("Hasil Selection:", a)

# Insertion Sort
def insertion_sort(arr):
    a = arr.copy()
    step = 1
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
        print_step(step, a)
        step += 1
    print("Hasil Insertion:", a)

# Quick Sort
def quick_sort(arr):
    def qs(a):
        if len(a) <= 1:
            return a
        pivot = a[len(a)//2]
        left = [x for x in a if x < pivot]
        mid = [x for x in a if x == pivot]
        right = [x for x in a if x > pivot]
        result = qs(left) + mid + qs(right)
        print("Step Quick:", result)
        return result

    result = qs(arr)
    print("Hasil Quick:", result)

# Merge Sort
def merge_sort(arr):
    def ms(a):
        if len(a) <= 1:
            return a
        mid = len(a)//2
        left = ms(a[:mid])
        right = ms(a[mid:])
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i]); i+=1
            else:
                result.append(right[j]); j+=1
        result += left[i:]
        result += right[j:]
        print("Step Merge:", result)
        return result

    result = ms(arr)
    print("Hasil Merge:", result)

# MAIN
n = int(input("Jumlah data: "))
data = list(map(int, input("Masukkan data: ").split()))

bubble_sort(data)
selection_sort(data)
insertion_sort(data)
quick_sort(data)
merge_sort(data)
