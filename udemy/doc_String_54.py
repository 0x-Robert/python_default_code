def example_func(param1, param2):

    """  Example function with types documented in the docstring.
    ## Args:
    ## param1 (int): The first parameter 
    ## param2 (str): The Second parameter

    #Returns:
    #bool: The return value. True for success, False otherwise
    """

    print(param1)
    print(param2)
    return True

#print(example_func.__doc__)  ##__doc__ 함수안에쓴 코멘트 출력됨
help(example_func)  ##help함수도 코멘트 출력해줌  , xml형식으로 만들어서 외부에서 읽게 하는것도 가능함



