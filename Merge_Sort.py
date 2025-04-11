def merge_sort(data_list):
    if len(data_list)>1:
        mid_index = len(data_list)//2
        left_list = data_list[:mid_index]
        right_list = data_list[mid_index:]
        #recursively sorts both left and right
        merge_sort(left_list)
        merge_sort(right_list)

        i=j=k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                data_list[k]=left_list[i]
                i+=1
            else:
                data_list[k]=right_list[j]
                j+=1
            k+=1
        while i<len(left_list):
            data_list[k]=left_list[i]
            i+=1
            k+=1

        while j<len(right_list):
                    data_list[k]=right_list[j]
                    j+=1
                    k+=1
    return data_list

ms = merge_sort([44,26,23,89,54,67,39,10]) #[10, 23, 26, 39, 44, 54, 67, 89]
print(ms)
