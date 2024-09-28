# vanilla gradient descent
from gradient import gradient
from fval import fun
from util import *
from args import *
def gradient_descent(x0, args):
    fval_best = 1e10
    maxIter = 500
    x = [x0_i for x0_i in x0]
    if ARGS.objectiveType == "square":
        step_size = 5e-1
    else:
        step_size = 5e-2
    eps = 1e-4
    distFval = 1e10
    contFval = 1e10
    iterNum = 0
    if ARGS.ismaxsat == 1: eps = 5e-5 * len(x0)
    
    while iterNum < maxIter:
        if not ARGS.unconstrained:
            oldx = x.copy()
            grad = gradient(x, args)
            x = [x[i] - grad[i] * step_size for i in range(len(x))]
            x = truncate(x)
            if norm([x[i] - oldx[i] for i in range(len(x))]) < eps: break
        else:
            grad = gradient(x, args)
            if norm(grad) < eps: break
            x = [x[i] - grad[i] * step_size for i in range(len(x))]
        contFval = fun(x, args)
        distFval = fun(rounding(x), args)
        #if distFval < 1 and ARGS.objectiveType == "square": break
        if distFval < 1: break
        # you can also break when contFval < 1/64
        iterNum += 1
        print("iter " + repr(iterNum) + " distFval " + repr(distFval) + " contFval " + repr(contFval)) # + " time " + repr(time.time()))
    return distFval, contFval, x, iterNum
