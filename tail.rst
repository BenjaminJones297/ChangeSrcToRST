tail
================

Purpose
----------------

Returns the last n rows of a matrix, dataframe or string array.

Format
----------------
.. function:: h = tail(X[,n])
    :param X: Matrix, dataframe or string array, the data to preview
    :type X: matrix 

    :param n: Optional input, the number of rows to return. Default = 5.If a negative number is supplied, all except the last n rowswill be returned.
    :type n: input 

    :return h: the last n rows of x (or all but the last n rows of x if n is negative)
    :rtype h: the last n rows of x (or all but the last n rows of x

Examples
----------------

Example 1
+++++++++++

::

       X = { 11 14,
             27 19,
             44 12,
             81 17,
             23 22,
             14 43 };


       tail(X);

::
   The above code will print:

       27.000000        19.000000
       44.000000        12.000000 
       81.000000        17.000000 
       23.000000        22.000000
       14.000000        43.000000



Example 2
+++++++++++

::


     tail(X, 3);

::
   will print out:

       81.000000        17.000000 
       23.000000        22.000000
       14.000000        43.000000



Example 3
+++++++++++

::


     tail(X, -2);

::
   will print out:

       11.000000        14.000000 
       27.000000        19.000000 
       44.000000        12.000000 
       81.000000        17.000000 
     

Remarks
-------

