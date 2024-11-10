
class CommonTools:
    
    @staticmethod
    def initPage(page:int) -> int:
        if page is None:
            return 1
        if page <= 0:
            return 1
        return page

    @staticmethod
    def initPageSize(pageSize:int) -> int:
        if pageSize is None:
            return 10
        if pageSize <= 0:
            return 10
        return pageSize
    
    @staticmethod
    def initSorts(sorts:list) -> list:
        sort_dict = {}
        if sorts is None or len(sorts) == 0:
            sort_dict['id'] = 'desc'
        else:
            for sort in sorts:
                if sort.get("prop") is None or sort.get("order") is None:
                    continue
                if sort.get("order") == 'asc':
                    sort_dict[sort.get("prop")] = 'asc'
                else:
                    sort_dict[sort.get("prop")] = 'desc'
        if len(sort_dict) == 0:
            sort_dict['id'] = 'desc'

        return sort_dict