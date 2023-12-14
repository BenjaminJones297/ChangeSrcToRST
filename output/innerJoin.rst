innerJoin
====================================

Purpose
----------------

Joins to matrices based upon user-specified key columns, with non-matching rows removed.

Format
----------------
.. function:: C = innerJoin(A, ca, B, cb)

    :param A: matrix to join
    :type A: matrix

    :param ca: Scalar, or vector, key columns in *A*.
    :type ca: scalar or vector

    :param B: matrix to join with *A*.
    :type B: matrix

    :param cb: scalar or vector, key columns in *B*.
    :type cb: scalar or vector

    :return C: matrix result of join of *A* and *B*
    :rtype C: matrix

Examples
----------------

Example 1
+++++++++++

::

    A = { 1 12 0.5,
          3 15 0.6,
          5 19 1.1,
          2 11 0.9 };
  
    B = { 7 0.3 5,
          2 1.1 1,
          9 0.1 3 };
  
    C = innerJoin(A, 1, B, 3);

  After the code above *C* equals:

::
  C = { 1 12 0.5 2 1.1
        3 15 0.6 9 0.1
        5 19 1.1 7 0.3 };

Remarks
-------


The first columns of the output matrix *C* will be the
columns of *A* in the same order as in A. The remaining
columns of *C* will be the columns of *B* with the
key columns removed.

