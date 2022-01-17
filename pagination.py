import math

class Pagination:

    def __init__(self, total_count, page, per_page =10):
        self.current_page = page
        self.next_page = page + 1
        self.previous_page = page - 1
        self.max_page = math.ceil(total_count/per_page)
        self.index_start = int(per_page) * int(page)
        self.index_end = int(per_page) * int(page) + int(per_page)

