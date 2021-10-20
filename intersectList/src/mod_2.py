class Module2:

    def __init__(self):
        """
        :param result:
        """
        self.result = []

    def intersect_number(self, list_odd, list_db3):
        """
        :return: list of common number between 2 list
        """
        self.result = list(set(list_odd) & set(list_db3))
        return self.result
