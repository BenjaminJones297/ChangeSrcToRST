between
==============================================

Purpose
----------------
Returns a binary matrix with a 1 if the corresponding element of X is between 'a' and 'b', with an option to specify
whether the ends are inclusive.

Format
----------------
.. function:: mask = between(X, left, right [, inclusive])

    :param x: Data.
    :type x: NxK matrix or dataframe.

    :param left: Lower limit of the range.
    :type left: 1x1 matrix or dataframe.

    :param right: Upper limit of the range.
    :type right: 1x1 matrix or dataframe.

    :param inclusive: Optional argument, specifies which limits are included in range. Default = ``"both"``. Options are:


        ========= ==============================================================
        "left"     Include lower limit only.
        "right"    Include upper limit only.
        "neither"  Do not include either limit.
        "both"     Include both limits.
        ========= ==============================================================


    :type inclusive: string

    :return mask: Equal to 1 if the corresponding element of X is in the specified range, otherwise a 0.
    :rtype mask: NxK matrix

Examples
----------------

Example 1: Select dates in a range
+++++++++++++++++++++++++++++++++++++++

::

    // Create file name with full path and load data
    fname = getGAUSSHome("examples/beef_prices.csv");
    beef = loadd(fname);

    beef = beef[1:5,.];
    print beef;

::

            date    beef_price 
          199201        116.64
          199202        114.49
          199203        111.11
          199204        108.17
          199205        107.76

::

    mask = between(beef[.,"date"], "1992-02", "1992-04");

By default, both endpoints are counted as a match.

::

    mask = 0
           1
           1
           1
           0

You can, however, specify if you would like the endpoints treated differently.

::

    // Set the final optional input, 'inclusive' to include only the right endpoint
    mask_inc_right = between(beef[.,"date"], "1992-02", "1992-04", "right");

::

    mask_inc_right = 0
                     0
                     1
                     1
                     0

:func:`between` can be used with :func:`selif` to filter data.

::

    // Select rows of the data "if" the mask value is non-zero
    beef_trim = selif(beef, mask);
    print beef_trim;

::

            date    beef_price 
          199202        114.49
          199203        111.11
          199204        108.17

    
Example 2: Multiple column use
+++++++++++++++++++++++++++++++++

::

    x  = { 100 200 300,
           40  50  60,
           7   8   9 };

    left = 25;

    right = 125;

    between(x, left, right);

The above code prints the following matrix to screen:

::

     1.0000000        0.0000000        0.0000000
     1.0000000        1.0000000        1.0000000
     0.0000000        0.0000000        0.0000000

.. seealso:: Functions :func:`recode`, :func:`counts`, :func:`reclassify`
