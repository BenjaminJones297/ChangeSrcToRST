rndKMp
========================

Purpose
----------------

Computes Poisson pseudo-random numbers

Format
----------------
.. function:: { x, newstate } = rndKMp(r, c, lambda, state)

    :param r: scalar, number of rows of resulting matrix
    :type r: scalar

    :param c: scalar, number of columns of resulting matrix.
    :type c: scalar

    :param lambda: shape argument for Poisson distribution.
    :type lambda: rxc matrix or rx1 vector or 1xc vector or scalar

    :param state: vector
    :type state: scalar or 500x1

    :return x: Poisson distributed random numbers.
    :rtype x: rxc matrix

    :return newstate: the updated state
    :rtype newstate: 500x1 vector

Examples
----------------
Remarks
-------

The properties of the pseudo-random numbers in *x* are -

E(x) = lambda, Var(x) = lambda
x = 0, 1, ....,  *lambda* > 0.

r and *c* will be truncated to integers if necessary.

rndKMp uses a KISS-Monster Algorithm to generate random
numbers. KISS initializes the sequence used in the recur-with-
carry Monster algorithm.

