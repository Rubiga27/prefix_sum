def prefix_sum(arr):
    pref_arr=[]
    pref_arr.append(arr[0])
    for i in range (1,len(arr)):
        pref_arr.append(pref_arr[i-1]+arr[i])
    return pref_arr
print(prefix_sum(list(map(int,input().split()))))