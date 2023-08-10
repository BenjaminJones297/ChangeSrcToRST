between
============================

Purpose
----------------

Returns a binary matrix with a 1 if the corresponding element of X is between 'a' and 'b', with an option to specify whether the ends are inclusive.

Format
----------------
.. function:: mask =  between(X, a, b [, inclusive])

    :param X: Data.
    :type X: matrix or dataframe

    :param left: the lower limit of the range
    :type left: matrix or dataframe

    :param right: the upper limit of the range
    :type right: matrix or dataframe

    :param inclusive: Optional argument
    :type inclusive: 

    :return mask: with a 1 if the corresponding element of X is in the specified range, otherwise a 0
    :rtype mask: NxK matrix

Examples
----------------

Example 1
+++++++++++

::

    X = { 2  6,
          4  3,
          1  5 };

    left = 2;
    right = 5;
    mask = between(x, left, right);

After the above code:

::

    mask = 1 0
           1 1
           0 1


Example 2
+++++++++++

::

    X = { 2  6,
          4  3,
          1  5 };

    left = 2;
    right = 5;
    inclusive = "right";
    mask = between(X, left, right, inclusive);

After the above code:

::

    mask = 0 0
           1 1
           0 1


Example 3
+++++++++++

::

    // Create a sequence of dates from March 4th, 2005
    // to March 9th, 2005
    X = seqaposix("2005-03-04", 1, "days", 6);

    left = "2005-03-06";
    right = "2005-03-08";
    mask = between(X, left, right);

After the above code:

::

    mask = 0
           0
           1
           1
           1
           1

Remarks
-------

