class ExpessionStorage():
    def __init__(self, size = 30) -> None:
        """
        Args:
            size (int, optional): Storage size. Defaults to 30.
        """
        self.size = size
        self.items = []
        self.statuses = ['success', 'fail']

    def add_item(self, item: dict):
        """
        Args:
            item (dict): Add the item to a storage.
        """
        if self.is_full():
            self.items = self.items[1:]     # offset and remove the element

        self.items.append(item)

    def get_items(self, limit: int = 30, status: str = None):
        """Return items filtered by quantity and status.
        Args:
            limit (int, optional): Defaults to 30.
            status (str, optional): Defaults to None.

        Raises:
            ValueError: Called with incorrect limit or status.

        Returns:
            list: List of returned items.
        """
        if (limit < 1 or limit > 30) or (status is not None and status not in self.statuses):
            raise ValueError("The limit or status is incorrect. Available values: 1 < limit < 30; available statuses: 'success', 'fail'.")

        elif status:
            # filter by status
            filtered = list()

            for item in self.items:
                if item.status.value == status:
                    filtered.append(item)

            return filtered[-limit:]        # slice by limit

        else:                               # if the status is not specified
            return self.items[-limit:]

    def is_full(self):
        """
        Returns:
            bool: True if the storage is full, otherwise returns False.
        """
        if len(self.items) == self.size:
            return True

        return False
