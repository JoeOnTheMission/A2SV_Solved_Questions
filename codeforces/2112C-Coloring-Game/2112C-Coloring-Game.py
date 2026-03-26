#print(arr[k],arr[j],arr[i])
                j -= 1
            else:
                #print(arr[k],arr[j],arr[i],"invalid")
                
                invalid += (j-k)
                k += 1
    print(all_pos - invalid)