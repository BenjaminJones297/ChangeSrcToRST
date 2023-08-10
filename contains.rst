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

    :param needles: Matrix, multi-dimensional array or string array,containing the elements to look for.
    :type needles: matrix 

    :return found: 1 if one or more elements from *needles* was found in *haystack* or 0 if no matches were found If *needles* contains only one element, the output from *contains* will be the same as the *==* operator for numeric data, or the *$==* operator for string data 
    :rtype found: scalar 

Examples
----------------

Example 1
+++++++++++

::

    Example 1: Find whether a matrix contains either 1 or -1

haystack = { 4 9  2

::
                -1 0  3
               2 2 -1


Example 2
+++++++++++

::

    //Create a string array containing a set of
    //possible missing value indicators
    missing = "" $| "NaN" $| ".";

    variables = "height" $| "weight" $| "" $| "age";

    //Search 'variables' for any of the elements
    //contained in 'missing'
    found = contains(categories, missing);

  After the above code *found* will equal 1 since 'variables' contains at least one

::
  element equal to one of the elements a null string ("") in this case of 'missing'.

  indexcat indnv ismiss reclassify
*/

Remarks
-------

