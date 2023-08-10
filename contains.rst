contains
================================

Purpose
----------------

Indicates whether one matrix, multidimensional array or string array contains any elements from another symbol.

Format
----------------
.. function:: found  = contains(haystack,needles)

    :param haystack: Matrix, multi-dimensional array or string array. Thesymbol to search
    :type haystack: matrix 

    :param needles: Matrix, multi-dimensional array or string array, containing the elements to look for.
    :type needles: matrix 

    :return **: the output from *contains* will be the same as the *==* operator for numeric data or the *$==* operator for string data 
    :rtype **: element 

Examples
----------------

Example 1
+++++++++++

::

    haystack = { 4 9  2,
                -1 0  3,
                 2 2 -1 };

    needles = { -1, 1 };

    //Search 'haystack' for any match of -1 or 1
    found = contains(haystack, needles);

  After the above code *found* will equal 1 since 'haystack' contains at least one

::
  element equal to one of the elements -1 in this case of 'needles'.

  Example 2: Find whether a string array contains one of multiple specified missing values

Remarks
-------

