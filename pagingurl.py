
class Paging():
    def getPagingList(self,url):
        pagingList = []
        offset = -20
        for x in range(49):
            offset += 20
            newUri = url + "?pagingOffset=" + str(offset)
            pagingList.append(newUri)
        return pagingList
