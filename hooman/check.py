import sys
from .result import Result

def check_scatter_chart(option, value):
    if option == 'hist_color':
        if value not in ['r', 'g', 'b']:
            raise Exception('"hist_color" takes only values r or g or b')


def check(function, option, value):
    if function == 'scatterchart':
        check_scatter_chart(option, value)

def check_params(params, options, funcname):
    for k in params:
        if k not in options:
            keys_list = ', '.join(list(options.keys()))
            sys.exit(f'Option "{k}" for {funcname} is not valid, available options: '+ keys_list)



def check_color(col):
    if isinstance(col, int) or isinstance(col, float):
        return Result.Ok((col, col, col))
    elif isinstance(col, list) or isinstance(col, tuple):
        if not len(col) in [1, 3]:
            Result.Fail('Fill takes only 1 or 3 parameters when using a list')
        if len(col) == 1:
            Result.Ok((col[0], col[0], col[0]))
        else:
            Result.Ok((col[0], col[1], col[2]))
    else:
        Result.Fail('Fill should be of type int, float, list or tuple')