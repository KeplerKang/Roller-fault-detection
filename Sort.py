str_in=input("请输入：")
arr1=[int(n) for n in str_in.split(',')]
#arr1=[13,87,54,15,16,65,32,24,10,9]
print("原始数列为：",arr1)
#冒泡排序
def msort(arr):
    n=len(arr)
    for j in reversed(range(n)):
        for i in range(j):
            if (arr[i] > arr[i + 1]):
                arr[i],arr[i + 1]=arr[i + 1] ,arr[i]

#快速排序
def partition(arr, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]
    for j in range(low, high):
        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]#中间值放中间
    return (i + 1)


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

#堆排序
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换
        heapify(arr, n, largest)  # 小的被换下后可能比下面的还小，应继续对下面节点调整


def heapSort(arr):
    n = len(arr)

    # 创建大顶堆
    for i in range(n-1, -1, -1):
        heapify(arr, n, i)

        # 交换元素，把元素依次交换到最后一个节点
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)


n = len(arr1)
quickSort(arr1, 0, n - 1)
print("快速排序后数列为：",arr1)
msort(arr1)
print("冒泡排序后数列为：",arr1)
heapSort(arr1)
print("堆排序后的数列为：",arr1)
