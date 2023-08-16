ols
============

Purpose
----------------

To compute least squares regression.

Format
----------------
.. function:: { vnam,m,b,stb,vc,stderr,sigma,cx,rsq,resid,dwstat } =ols(dataset,depvar,indvars)
    :param dataset: string, name of data setIf this is a null string, the procedure assumesthat the actual data has been passed in thenext two arguments
    :type dataset: string 

    :param depvar: dependent variable.If dataset contains the name of a data set, this isinterpreted as:string, name of dependent variableorscalar, index of dependent variable. If scalar 0,the last column of the data set will be used.If dataset is a null string or 0, this isinterpreted as:Nx1 vector, the dependent variable
    :type depvar: set 

    :param indvars: If ascalar 0 is passed, all columns of the data setwill be used except for the one used for thedependent variable.If dataset is a null string or 0, this isinterpreted as:NxK matrix, the independent variablesDefaults are provided for the following global inputvariables so they can be ignored unless you need controlover the other options provided by this procedure.
    :type indvars: passed 

    :param __altnam: If __con is 1, this must be (K+2)x1.The dependent variable is the last element.This has an effect only if the data are passedin as matrices.
    :type __altnam: 1 

    :param __con: no constant term will be added, D = K.A constant term is always used inconstructing the moment matrix m.
    :type __con: added 

    :param __miss: pairwise deletion, this is equivalent tosetting missings to 0 when calculating m.The number of cases computed is equal tothe total number of cases in the data set.
    :type __miss: deletion 

    :param __row: you can use __rowto control this if you want to get exactly thesame rounding effects between several runs.
    :type __row: you

    :param __output: do not print statistics.
    :type __output: do

    :param _olsres: resid = 0, dwstat = 0.
    :type _olsres: 0 

    :return vnam: (k+2)x1 or (k+1)x1 character vector the variable names used in the regression. If a constant term is used this vector will be (K+2)x1, and the first name will be "CONSTANT". The last name will be the name of the dependent variable
    :rtype vnam: (k+2)x1 or (k+1)x1 character vector

    :return m: MxM matrix where M = K+2, the moment matrix constructed by calculating x*x where x is a matrix containing all useable observations and having columns in the order: constant ~ indvars ~ depvar ------------------------------------------------------ (1.0) ~ (independent variables) ~ (dependent variable) A constant term is always used in computing m, even if __CON = 0
    :rtype m: MxM matrix matrix

    :return b: dx1 vector the least squares estimates of parameters Error handling is controlled by the low order bit of the trap flag TRAP 0 terminate with error message TRAP 1 return scalar error code in b 30 system singular 31 system underdetermined 32 same number of columns as rows 33 too many missings 34 file not found 35 no variance in an independent variable The system can become underdetermined if you use listwise deletion and have missing values. In that case it is possible to skip so many cases that there are fewer useable rows than columns in the data set
    :rtype b: Dx1 vector

    :return stb: kx1 vector the standardized coefficients
    :rtype stb: Kx1 vector

    :return vc: DxD matrix the variance-covariance matrix of estimates
    :rtype vc: DxD matrix matrix

    :return stderr: dx1 vector the standard errors of the estimated parameters
    :rtype stderr: Dx1 vector

    :return sigma: scalar standard deviation of residual
    :rtype sigma: scalar

    :return cx: (K+1)x(K+1) matrix correlation matrix of variables in the order: independent variables ~ dependent variable
    :rtype cx: (k+1)x(k+1) matrix matrix

    :return rsq: scalar R square, coefficient of determination
    :rtype rsq: scalar

    :return resid: residuals resid = y - x * b If _olsres = 1, the residuals will be computed If the data is taken from a data set, a new data set will be created for the residuals, using the name in the global string variable _olsrnam. The residuals will be saved in this data set as an Nx1 column. The resid return value will be a string containing the name of the new data set containing the residuals If the data is passed in as a matrix, the resid return value will be the Nx1 vector of residuals
    :rtype resid: residuals Nx1 column.

    :return dwstat: scalar Durbin-Watson statistic
    :rtype dwstat: scalar

Examples
----------------

Example 1
+++++++++++

::

             y = { 2,
                    3,
                    1,
                    7,
                    5 };

             x = { 1 3 2,
                    2 3 1,
                    7 1 7,
                    5 3 1,
                    3 5 5 };


 output file = ols.out reset;
 call ols(0yx);
 output off;

::
              In this example the output from ols was put into a
              file called ols.out as well as being printed on the
              screen.  This example will to compute a least squares
              regression of y on x.  The returned values were
              discarded by using a call statement.



Example 2
+++++++++++

::

              data = "olsdat";
              depvar = { score };
              indvars = { region,age,marstat };
              _olsres = 1;
              output file = lpt1 on;
              { nam,m,b,stb,vc,std,sig,cx,rsq,resid,dbw } =

    ols(datadepvarindvars);
output off;

::
              In this example the data set olsdat.dat was used
              to compute a regression. The dependent variable
              is "score". The independent variables are:
              "region" "age" and "marstat".  The residuals
              and Durbin-Watson statistic will be computed.
              The output will be sent to the printer as well as
              the screen and the returned values are assigned
              to variables.


Remarks
-------

No output file is modified, opened, or closed by this
procedure.  If you want output to be placed in a file
you need to open an output file before calling ols.
If a column of constant value has been included among
the independent variables, this variable will be
deleted.

**  See Also:   olsqr
**  See Also:   olsqr
