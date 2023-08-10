rndKMbeta
====================================

Purpose
----------------

Computes beta pseudo-random numbers.

Format
----------------
.. function:: { x, newstate } = rndKMbeta(r, c, a, b, state)

    :param r: scalar, number of rows of resulting matrix
    :type r: scalar

    :param c: scalar, number of columns of resulting matrix.
    :type c: scalar

    :param a: first shape argument for beta distribution.
    :type a: rxc matrix or rx1 vector or 1xc vector or scalar

    :param b: second shape argument for beta distribution.
    :type b: rxc matrix or rx1 vector or 1xc vector or scalar

    :param state: vector
    :type state: scalar or 500x1

    :return x: beta distributed random numbers.
    :rtype x: rxc matrix

    :return newstate: the updated state
    :rtype newstate: 500x1 vector

Examples
----------------
Remarks
-------

The properties of the pseudo-random numbers in *x* are -

a                      (a * b)
E(x) = ------- ,   Var(x) = -------------------------
a + *b*                (a + *b* + 1) * (a + b)^2

0 < *x* < 1,  *a* > 0,  *b* > 0

r and *c* will be truncated to integers if necessary.

rndKMbeta uses *a* KISS-Monster Algorithm to generate random
numbers. KISS initializes the sequence used in the recur-with-
carry Monster algorithm.

