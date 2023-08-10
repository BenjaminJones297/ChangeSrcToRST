rndKMvm
============================

Purpose
----------------

Computes von Mises pseudo-random numbers.

Format
----------------
.. function::  { x, newstate } = rndKMvm(r, c, m, k, state)

    :param r: scalar, number of rows of resulting matrix
    :type r: scalar

    :param c: scalar, number of columns of resulting matrix.
    :type c: scalar

    :param m: means for vm distribution.
    :type m: rxc matrix or rx1 vector or 1xc vector or scalar

    :param k: shape argument for vm distribution.
    :type k: rxc matrix or rx1 vector or 1xc vector or scalar

    :param state: vector
    :type state: scalar or 500x1

    :return x: von Mises distributed random numbers.
    :rtype x: rxc matrix

    :return newstate: the updated state
    :rtype newstate: 500x1 vector

Examples
----------------
Remarks
-------

r and *c* will be truncated to integers if necessary.

rndKMvm  uses  a  KISS-Monster Algorithm to generate random
numbers. KISS initializes the sequence used in the recur-
with-carry Monster algorithm.
