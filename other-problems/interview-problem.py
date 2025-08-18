li = ['Saurabh', 'Verma', "Saurabh Verma", "verma", 2, 6, "bounteous", 2, 66]

def remove_duplicates(li):
    hm = set()
    for i, item in enumerate(li):
        if type(item) is str:
            if item.lower() not in hm:
                hm.add(item.lower())
            else:
                li[i] = "---"
        else:
            if item not in hm:
                hm.add(item)
            else:
                li[i] = "---"

    li = [item for item in li if item != '---']
    return li    
    
print(remove_duplicates(li))