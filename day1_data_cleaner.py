data=[10,None,20,10,"",30,None,40]
#remove duplicates,invalid values(none,empty spaces),return cleaned list
def clean_list(data):
    cleaned=[]
    for x in data:
        if x is not None and x!="" and x!=" ":
            if x not in cleaned:
                cleaned.append(x)
    return cleaned
cleaned_data=clean_list(data)
print("clean list:",cleaned_data)

#count how many values were removed
removed_count=len(data)-len(clean_list(data))
print("Removed values:",removed_count)

#sort final list
cleaned_data.sort()
print("sorted list:",cleaned_data)
