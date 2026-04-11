#print(children)
    is_leaf = [False] * (n + 1)
    for i in range(1, n + 1):
        if children[i] == 0:
            is_leaf[i] = True
    #print(is_leaf)

    for i in range(1, n + 1):
            if not is_leaf[i]:
                leaf_children = 0
                # Count leaf children
                for j in range(len(parents)):
                    # p[j] is parent of node j+2
                    if parents[j] == i and is_leaf[j + 2]:
                        leaf_children += 1
                    #print(i,j,leaf_children)
                if leaf_children < 3:
                    print("No")
                    break
    else:
        print("Yes")