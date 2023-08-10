rndKMnb
============================

Purpose
----------------

Computes negative binomial pseudo-random numbers.

Format
----------------
.. function:: { x, newstate } = rndKMnb(r, c, k, p, state)

    :param r: scalar, number of rows of resulting matrix
    :type r: scalar

    :param c: scalar, number of columns of resulting matrix.
    :type c: scalar

    :param k: "event" argument for negative binomial distribution.
    :type k: rxc matrix or rx1 vector or 1xc vector or scalar

    :param p: "probability" argument for negative binomial distribution.
    :type p: rxc matrix or rx1 vector or 1xc vector or scalar

    :param state: vector
    :type state: scalar or 500x1

    :return x: negative binomial distributed random numbers.
    :rtype x: rxc matrix

    :return newstate: the updated state
    :rtype newstate: 500x1 vector

Examples
----------------
Remarks
-------

The properties of the pseudo-random numbers in *x* are -

k * *p*                  *k* * p
E(x) = --------- , Var(x) = -----------
(1 - p)              (1 - p)^2

x = 0, 1, ...,   *k* > 0,  0 < *p* < 1

r and *c* will be truncated to integers if necessary.

rndKMnb uses a KISS-Monster Algorithm to generate random
numbers. KISS initializes the sequence used in the recur-with-
carry Monster algorithm.

