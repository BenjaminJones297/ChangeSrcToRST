rndKMgam
================================

Purpose
----------------

Computes Gamma pseudo-random numbers.

Format
----------------
.. function::  { x, newstate } = rndKMgam(r, c, alpha, state)

    :param r: scalar, number of rows of resulting matrix
    :type r: scalar

    :param c: scalar, number of columns of resulting matrix.
    :type c: scalar

    :param alpha: shape argument for gamma distribution.
    :type alpha: rxc matrix or rx1 vector or 1xc vector or scalar

    :param state: vector
    :type state: scalar or 500x1

    :return x: gamma distributed random numbers.
    :rtype x: rxc matrix

    :return newstate: the updated state
    :rtype newstate: 500x1 vector

Examples
----------------
Remarks
-------

The properties of the pseudo-random numbers in *x* are -

E(x) = alpha, Var(x) = alpha
x > 0,  *alpha* > 0.

To generate gamma(alpha, theta) pseudo-random numbers where theta
is a scale parameter, multiply the result of rndgam by theta.
Thus

z = theta * rndgam(1, 1, alpha);

has the properties

E(z) = *alpha* * theta, Var(z) = *alpha* * theta ^ 2
z > 0, *alpha* > 0, theta > 0.

r and *c* will be truncated to integers if necessary.

rndKMgam uses a KISS-Monster Algorithm to generate random
numbers. KISS initializes the sequence used in the recur-with-
carry Monster algorithm.

