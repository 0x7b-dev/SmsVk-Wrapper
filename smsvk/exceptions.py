class NoBalance(Exception):
    """Balance smaller than price"""
    pass


class NoNumbers(Exception):
    """Service doesn't have free numbers for this service"""
    pass

class Error(Exception):
    """Server returns Error"""
    pass