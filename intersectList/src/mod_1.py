class Module1:

    def __init__(self, min_number, max_number):
        """
        :param min_number:
        :param max_number:
        """
        self.list_number_odd = []
        self.list_number_db3 = []
        self.min_number = min_number
        self.max_number = max_number

    def check(self):
        """
        :return: 2 list of odd number and number divisible by 3
        """
        if self.max_number < self.min_number:
            print('Warning: Min must less than max!')
        else:
            for number in range(self.min_number, self.max_number):
                if number % 2 == 1:
                    self.list_number_odd.append(number)
                if number % 3 == 0:
                    self.list_number_db3.append(number)
        return self.list_number_odd, self.list_number_db3
