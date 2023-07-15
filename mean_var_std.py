import numpy
import numpy as np


def list_to_matrix(lst, rows, columns):
    return np.array(lst).reshape(rows, columns)


def calculate(lst):
    """
    :param
    mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
    This Matrix is being represented with a numpy array because numpy matrix is being deprecated as of 3.5.
    :list: The input of the function should be a list containing 9 digits. The function should convert the list
    into a 3 x 3 Numpy array :

    :return:  The returned dictionary should follow this format:
    { 'mean': [axis1, axis2, flattened],
    'variance': [axis1, axis2, flattened],
    'standard deviation': [axis1, axis2, flattened],
    'max': [axis1, axis2, flattened],
    'min': [axis1, axis2, flattened],
    'sum': [axis1, axis2, flattened] }
    """
    if len(lst) < 9:
        ValueError(lst)
    calculations = {}
    funct = {'mean': np.mean, 'variance': np.var, 'standard deviation': np.std,
             'max': np.max, 'min': np.min, 'sum': np.sum}
    # A function which converts the given list to a Numpy Array, NOT MATRIX, because Matrix is being deprecated as of
    # the Python 3.5 update. In essence Array can function in all the way Matrix could uniquely function before and
    # there for has no unique purpose.
    matrix = list_to_matrix(lst, 3, 3)

    # Iterates through a dictionary of the functions, performs the functions on axis 1, 2, and the overall matrix, then
    # appends this result to the calculations dictionary
    for f in funct:
        calculations[f] = list(funct[f](matrix, axis=0)), list(funct[f](matrix, axis=1)), funct[f](matrix)
    return calculations, funct['mean'](lst)
