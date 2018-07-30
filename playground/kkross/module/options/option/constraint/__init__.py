import logging

from kkross.exceptions import ConstraintError

log = logging.getLogger('kkross;module')

# -------------------------------------------------------------------------------------------------
class Constraint(object):
    '''Constraint for module option'''

    def __init__(self, constraint_raw):
        self.constraint_raw = constraint_raw

    def check(self, value):
        '''Checks if value meets constraint - returns True or False'''
