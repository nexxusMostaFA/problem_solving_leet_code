import self
def hIndex(self, citations):
    size = len(citations)
    # 4
    while size >= 0:
        counter = 0

        for citation in citations:
            if citation >= size:
                counter += 1

        if counter >= size:
            return size

        size -= 1
    return 0




list =  [1,3,1]
print(hIndex(self,list))





