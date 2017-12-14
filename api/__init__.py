account = Account()


def getAccount():
    return account


class Account:

    """ Hooks for API """

    def balance(self):
        """ Get balance of Account """
        return 0

    def transactions(self):
        """ Get bundles in/out associated with address """
        return []
