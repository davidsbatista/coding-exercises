__author__ = 'dsbatista'

def bubble_sort(arr_n):
    while True:
        swapped = False
        for i, x in enumerate(arr_n):
            if i+1 <= len(arr_n)-1:
                print x, arr_n[i+1]
                if x > arr_n[i+1]:
                    arr_n[i] = arr_n[i+1]
                    arr_n[i+1] = x
                    swapped = True
        if swapped is False:
            return arr_n
            break


def main():
    x_array = [2, 2, 2, 2, 2, 2, 2, 234, 23, 534, 2, 1, 23, 4, 34, 4, 2, 123, 2, 32]
    print bubble_sort(x_array)

if __name__ == "__main__":
    main()
