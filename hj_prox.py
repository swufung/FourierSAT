# vanilla HJ_prox
from fval import fun
from HJ_utils import compute_prox
from util import *
from args import *

def hj_prox(x0, args):
    fval_best = 1e10
    maxIter = int(1e4)
    x = x0
    eps = 1e-4
    distFval = 1e10
    contFval = 1e10
    iterNum = 0
    # if ARGS.ismaxsat == 1: eps = 5e-5 * len(x0)

    dist_fval_best = 1e10
    cont_fval_best = 1e10
    
    while iterNum < maxIter:
        if not ARGS.unconstrained:
            x, *_ = compute_prox(x, fun, t=1e-1, delta=1e-2, int_samples=int(1e4), alpha=1.0, linesearch_iters=0)
            x = truncate(x)
        else:
            x, *_ = compute_prox(x, fun, t=1e-1, delta=1e-2, int_samples=int(1e4), alpha=1.0, linesearch_iters=0)
        contFval = fun(x, args)
        distFval = fun(rounding(x), args)

        if distFval < dist_fval_best:
            x_best = x

        dist_fval_best = min(dist_fval_best, distFval)
        cont_fval_best = min(cont_fval_best, contFval)


        #if distFval < 1 and ARGS.objectiveType == "square": break
        if distFval < 1: break
        # you can also break when contFval < 1/64
        iterNum += 1
        print("iter " + repr(iterNum) + " distFval " + repr(distFval) + " contFval " + repr(contFval)) # + " time " + repr(time.time()))



    return dist_fval_best, cont_fval_best, x_best, iterNum
