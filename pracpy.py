""" This library is for the purpose of PHY244: Practical Physics 1. """
from typing import Union
import numpy as np
# import sympy as sp
# import matplotlib.pyplot as plt
# from scipy.optimize import curve_fit


def load_file(names: list, file: str) -> None:
    """
    Saves the columns as arrays assigned to the given variables. The length of the tuple should be
    equal to the number of columns in file
    :param names: the variables to be assigned columns to
    :param file: the csv file to be unpacked
    """
    # data = np.loadtxt(file, delimiter=',', encoding='utf-8')
    # names = []
    # for i in range(0, len(names) - 1):
    #     names[i] = data[i]


def combine_unc(ep: Union[np.array, int], ea: Union[np.array, int]) -> \
        Union[np.array, int]:
    """
    Calculates the combined uncertainty from the error of precision and error of accuracy:

    u(x) = sqrt((ua(x))^2 + (up(x))^2)

    where ua(x) is the error of accuracy and up(x) is the error of precision, and stores the
    combined uncertainties into an array
    :param ep: the error of precision
    :param ea: the error of accuracy
    :return: the combined uncertainty

    >>> combine_unc(0.33333, 0.000001)
    0.33333000000150004
    """
    return np.sqrt(ep ** 2 + ea ** 2)


def round_sig(num: Union[np.array, float, int], sf: int) -> Union[np.array, float]:
    """
    Rounds the given float or array of floats to the given number of significant figures
    :param num: a given float or array of floats
    :param sf: number of significant figures
    :return: the array or float rounded to the given number of significant figures.

    >>> round_sig(0.03089, 1)
    0.03
    >>> round_sig(-53390, 3)
    -53400
    >>> round_sig([0.03089, -53390], 1)
    [0.03, -53400]
    """
    if num is float or int:
        return round(num, sf - int(np.floor(np.log10(abs(num)))) - 1)
    elif num is np.array:
        # rounded_array = np.array([])
        for old_num in num:
            round_sig(old_num, sf)
        #     new_num = round(old_num, sf - int(np.floor(np.log10(abs(old_num)))) - 1)
        #     np.append(rounded_array, new_num)
        # return rounded_array


def save_data(columns: list[np.array], file_name: str, header: str, ) -> None:
    """
    Saves the given arrays into a file with the given file name as columns. The file has header
    with the given header
    :param columns:
    :param file_name: the file name to be save to
    :param header: the header of the file
    """
    data = np.vstack([columns]).T
    np.savetxt(file_name, data, delimiter=",", header=header)


def calculate_chi_squared(n: int, y: np.array, f_x: np.array,
                          sigma: np.array, display_text: True) -> float:
    """
    Calculates the reduced chi squared
    :param display_text: displays a message reporting the calculated chi-squared if true
    :param n: Number of parameters
    :param y: 1-dimensional array of the measured values of y
    :param f_x: 1-dimensional array of the predictions of y using the measured values of x
    :param sigma: The errors on y
    :return: reduced chi squared as a float
    """
    reduced_chi_squared = np.sum(((y - f_x) / sigma) ** 2) / (y.size - n)
    if display_text:
        print("The calculated reduced chi squared of the fitting is " + str(reduced_chi_squared))
    return reduced_chi_squared


# def get_best_fit(y: np.array, yerr: np.array, x: np.array, xerr: np.array, guess=None) -> None:
#     """..."""
