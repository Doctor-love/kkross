import logging

from kkross.exceptions import ConstraintError
from kkross.module.option.constraint import Constraint

log = logging.getLogger('kkross;constraint')

# -------------------------------------------------------------------------------------------------
def parse_constraints(constraints_raw):
    '''Does some basic parsing of contraints and returns constraint objects'''

    if not type(constraints_raw) is list:
        raise ConstraintError('Constraints data is invalid (list required)')

    constraints = []

    for constraint_raw in constraints_raw:
        if not type(constraint_raw) is dict:
            raise ConstraintError('Constraint data is invalid (dictionary required)')

        for req_property in ['constraint_type', 'options']:
            if not req_property in constraint_raw:
                raise ConstraintError(
                    'Constraint data is invalid, property "%s" not found' % req_property)

        if not type(constraint_raw['constraint_type']) is str:
            raise ConstraintError('Constraint property "constraint_type" must be a string')

        constraints.append(Constraint(constraint_raw))

    return constraints
