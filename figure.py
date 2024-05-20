import math

class Line:
    """
    변의 길이 값을 관리하는 클래스입니다.
    """
    __length = 1

    def __init__(self, length):
        """ 변의 길이의 초기값을 설정해주는 함수입니다.
        Args: 
            length(int 또는 float): 변의 길이를 받아오는 변수입니다.
        return:

        """
        if ((isinstance(length, int) or isinstance(length, float)) and length > 0):
            self.__length = length
        else: self.__length = 1


    def set_length(self, length):
        """ 변의 길이를 설정해주는 함수입니다.
        Args: 
            length(int 또는 float): 변의 길이를 받아오는 변수입니다.
        return:

        """
        if ((isinstance(length, int) or isinstance(length, float)) and length > 0):
            if length > 0: self.__length = length

    def get_length(self):
        """ 변의 길이를 반환해주는 함수입니다.
        Args: 
            
        return:
            변의 길이를 반환합니다.
        """
        return self.__length

def area_square(line):
    """ 길이를 입력 받아 정사각형의 넓이를 계산하는 함수입니다.
    Args: 길이를 얻기 위한 매개변수입니다.
        line (class 타입): Line객체를 받아오는 변수입니다. 
    return:
        구한 넓이 값을 반환합니다.
    """
    if not isinstance(line, Line): return 0
    result = line.get_length() ** 2
    return result

def area_circle(line):
    """ 길이를 입력 받아 원의 넓이를 계산하는 함수입니다.
    Args: 길이를 얻기 위한 매개변수입니다.
        line (class 타입): Line객체를 받아오는 변수입니다. 
    return:
        구한 넓이 값을 반환합니다.
    """
    if not isinstance(line, Line): return 0
    result = math.pi * (line.get_length() ** 2)
    return result

def area_regular_triangle(line):
    """ 길이를 입력 받아 점삼각형의 넓이를 계산하는 함수입니다.
    Args: 길이를 얻기 위한 매개변수입니다.
        line (class 타입): Line객체를 받아오는 변수입니다. 
    return:
        구한 넓이 값을 반환합니다.
    """
    if not isinstance(line, Line): return 0
    result = math.sqrt(3) / 4 * (line.get_length() ** 2)
    return result

    