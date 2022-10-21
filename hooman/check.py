import sys
from .result import Result
import inspect
import traceback


def check_scatter_chart(option, value):
    if option == "hist_color":
        if value not in ["r", "g", "b"]:
            raise Exception('"hist_color" takes only values r or g or b')


def check(function, option, value):
    if function == "scatterchart":
        check_scatter_chart(option, value)


def check_params(params, options, funcname):
    for k in params:
        if k not in options:
            keys_list = ", ".join(list(options.keys()))
            sys.exit(
                f'Option "{k}" for {funcname} is not valid, available options: '
                + keys_list
            )


def check_color(col):
    # must be cleared
    if isinstance(col, int) or isinstance(col, float):
        pass
    if isinstance(col, list) or isinstance(col, tuple):
        if not len(col) in [1, 3]:
            return Result.Fail("Fill takes only 1 or 3 parameters when using a list")
        if len(col) == 1:
            if isinstance(col, tuple) or isinstance(col, list):
                if (isinstance(col[0], tuple) or isinstance(col[0], list)) and len(col[0]) in [3]:
                    return Result.Ok(col)
                elif isinstance(col[0], int):
                    val = (col[0], col[0], col[0])
                    return Result.Ok(val)
                else:
                    raise Exception('color must be like fill(100) or fill((100, 100, 255)) or fill(100, 100, 255)')
            return Result.Ok((col[0], col[0], col[0]))
        else:
            return Result.Ok((col[0], col[1], col[2]))
    else:
        return Result.Fail("Fill should be of type int, float, list or tuple")


def check_value(val, type_, value_name, range_=None):
    if not isinstance(value_name, str):
        return Result.Fail("Value name should be of type string")
    else:
        if not isinstance(type_, list):
            if not isinstance(val, type_):
                return Result.Fail(
                    f'Value "{val}" for {value_name} should be of type {type_}'
                )
            if type_ in [int, float]:
                if type(range_) in [list, tuple]:
                    if len(range_) == 2:
                        if not range_[0] < val < range_[1]:
                            return Result.Fail(
                                f"Value of {value_name} should be between {range_[0]} and {range_[1]}"
                            )
                    elif len(range_) == 0:
                        pass
                    else:
                        return Result.Fail("Range takes [n1, n2] or []")
                else:
                    return Result.Fail("Range should be of type list or tuple")
        elif isinstance(type_, list):
            results = []
            for t in type_:
                if not isinstance(val, t):
                    results.append(0)
                else:
                    results.append(1)
            if not any(results):
                return Result.Fail(
                    f'Value "{val}" for {value_name} should be of type {type_}'
                )

    return Result.Ok(val)


def verify_func_param(method, param_types, locals_):
    try:
        param_names = inspect.getfullargspec(method)[0]
        for param in param_names:
            if param not in ["self"]:
                verif = check_value(
                    locals_[param],
                    param_types[param][0],
                    param,
                    range_=param_types[param][1],
                )
                if not verif.success:
                    raise Exception(verif.error)
    except Exception as e:
        filename = traceback.extract_stack()[0].filename
        line = traceback.extract_stack()[0].line
        lineno = traceback.extract_stack()[0].lineno

        print(
            "Hooman",
            type(e).__name__,  # TypeError
            "in file",
            filename,  # /tmp/example.py
            "at line",
            lineno,  # 2
        )
        print(">>>", line)
        print(str(e))
        sys.exit()


def verify_color(colors=[]):
    for color in colors:
        try:
            verif = check_color(color)
            if not verif.success:
                raise Exception(verif.error)
        except Exception as e:
            filename = traceback.extract_stack()[0].filename
            line = traceback.extract_stack()[0].line
            lineno = traceback.extract_stack()[0].lineno

            print(
                "Hooman",
                type(e).__name__,  # TypeError
                "in file",
                filename,  # /tmp/example.py
                "at line",
                lineno,  # 2
            )
            print(">>>", line)
            print(str(e))
            sys.exit()
