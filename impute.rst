impute
========================

Purpose
----------------

Fills missing values in columns of a matrix with a choice of imputation methods.

Format
----------------
.. function:: x_full= impute(x [, method, depvars, iCtl])
    :param x: NxK matrix, multidimensional array
    :type x: matrix 

    :param method: Optional string input, the imputation method to use. Valid options include:"mean" (default)."median""mode""predict""pmm""lrd"
    :type method: input 

    :param depvars: Optional argument
    :type depvars: 

    :param iCtl: Optional argument
    :type iCtl: 

    :return x_full: NxK matrix or multidimensional array with all missing values filled
    :rtype x_full: matrix or multidimensional matrix

Examples
----------------
Remarks
-------

