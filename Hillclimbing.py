def findLocalMaximaMinima(n, arr):

    mx = []
    mn = []

    if(arr[0] > arr[1]):
        mx.append(0)
    elif(arr[0] < arr[1]):
        mn.append(0)

    for i in range(1, n-1):


        if(arr[i-1] > arr[i] < arr[i+1]):
            mn.append(i)

        elif(arr[i-1] < arr[i] > arr[i+1]):
            mx.append(i)

    if(arr[-1] > arr[-2]):
        mx.append(n-1)
    elif(arr[-1] < arr[-2]):
        mn.append(n-1)

    if(len(mx) > 0):
        print("Points of Local maxima"\
            "are: ", end ='')
        print(*mx)
    else:
        print("There are no points of"\
             " Local maxima.")

    if(len(mn) > 0):
        print("Points of Local minima"\
            "are : ", end='')
        print(*mn)
    else:
        print("There are no points"\
            " of Local minima.")

if __name__ == '__main__':

    N = 9
    arr = [10, 20, 15, 14, 13, 25, 5, 4, 3]

    findLocalMaximaMinima(N, arr)
