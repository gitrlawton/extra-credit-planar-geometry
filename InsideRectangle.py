# PROGRAMMER: Ryan Lawton

# IMPORT STATEMENTS






class InsideRectangle:

# CONSTRUCTOR

    def __init__(self, width, height, offset, x_centroid, y_centroid):
        if type(width) is not float:
            raise TypeError(
                "InsideRectangle.py __init__ width - must be a float."
            )
        if width <= 0:
            raise ValueError(
                "InsideRectangle.py __init__ width - must be greater than 0."
            )
        if type(height) is not float:
            raise TypeError(
                "InsideRectangle.py __init__ height - must be a float."
            )
        if height <= 0:
            raise ValueError(
                "InsideRectangle.py __init__ height - must be greater than 0."
            )   
        if type(offset) is not float:
            raise TypeError(
                "InsideRectangle.py __init__ offset - must be a float."
            )
        if offset <= 0:
            raise ValueError(
                "InsideRectangle.py __init__ offset - must be greater than 0."
            )
        if type(x_centroid) is not float:
            raise TypeError(
                "InsideRectangle.py __init__ x_centroid - must be a float."
            )
        if type(y_centroid) is not float:
            raise TypeError(
                "InsideRectangle.py __init__ y_centroid - must be a float."
            )   
        
        self.__width = width
        self.__height = height
        self.__offset = offset
        self.__x_centroid = x_centroid
        self.__y_centroid = y_centroid

# INSTANCE METHODS
    
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height
    
    def get_offset(self):
        return self.__offset
    
    def get_x_centroid(self):
        return self.__x_centroid
    
    def get_y_centroid(self):
        return self.__y_centroid
    
    def rectangle_points_clockwise(self):    
        top_left_point = (self.__x_centroid - (self.__width / 2), self.__y_centroid + (self.__height / 2))
        top_right_point = (self.__x_centroid + (self.__width / 2), self.__y_centroid + (self.__height / 2))
        bottom_left_point = (self.__x_centroid - (self.__width / 2), self.__y_centroid - (self.__height / 2))
        bottom_right_point = (self.__x_centroid + (self.__width / 2), self.__y_centroid - (self.__height / 2))
        
        return [top_right_point, bottom_right_point, bottom_left_point, top_left_point]
    
    def rectangle_points_counterclockwise(self):
        top_left_point = (self.__x_centroid - (self.__width / 2), self.__y_centroid + (self.__height / 2))
        top_right_point = (self.__x_centroid + (self.__width / 2), self.__y_centroid + (self.__height / 2))
        bottom_left_point = (self.__x_centroid - (self.__width / 2), self.__y_centroid - (self.__height / 2))
        bottom_right_point = (self.__x_centroid + (self.__width / 2), self.__y_centroid - (self.__height / 2))
        
        return [top_left_point, bottom_left_point, bottom_right_point, top_right_point]
    
    def dashed_rectangle_points_clockwise(self):
        dashed_width = self.__width + (self.__offset * 2)
        dashed_height = self.__height + (self.__offset * 2)
        
        top_left_point = (self.__x_centroid - (dashed_width / 2), self.__y_centroid + (dashed_height / 2))
        top_right_point = (self.__x_centroid + (dashed_width / 2), self.__y_centroid + (dashed_height / 2))
        bottom_left_point = (self.__x_centroid - (dashed_width / 2), self.__y_centroid - (dashed_height / 2))
        bottom_right_point = (self.__x_centroid + (dashed_width / 2), self.__y_centroid - (dashed_height / 2))
        
        return [top_right_point, bottom_right_point, bottom_left_point, top_left_point]
    
    def dashed_rectangle_points_counterclockwise(self):
        dashed_width = self.__width + (self.__offset * 2)
        dashed_height = self.__height + (self.__offset * 2)
        
        top_left_point = (self.__x_centroid - (dashed_width / 2), self.__y_centroid + (dashed_height / 2))
        top_right_point = (self.__x_centroid + (dashed_width / 2), self.__y_centroid + (dashed_height / 2))
        bottom_left_point = (self.__x_centroid - (dashed_width / 2), self.__y_centroid - (dashed_height / 2))
        bottom_right_point = (self.__x_centroid + (dashed_width / 2), self.__y_centroid - (dashed_height / 2))
        
        return [top_left_point, bottom_left_point, bottom_right_point, top_right_point]
    
    def dotted_rectangle_points_clockwise(self):
        dotted_width = self.__width + (self.__offset * 4)
        dotted_height = self.__height + (self.__offset * 4)
        
        top_left_point = (self.__x_centroid - (dotted_width / 2), self.__y_centroid + (dotted_height / 2))
        top_right_point = (self.__x_centroid + (dotted_width / 2), self.__y_centroid + (dotted_height / 2))
        bottom_left_point = (self.__x_centroid - (dotted_width / 2), self.__y_centroid - (dotted_height / 2))
        bottom_right_point = (self.__x_centroid + (dotted_width / 2), self.__y_centroid - (dotted_height / 2))
        
        return [top_right_point, bottom_right_point, bottom_left_point, top_left_point]
    
    def dotted_rectangle_points_counterclockwise(self):
        dotted_width = self.__width + (self.__offset * 4)
        dotted_height = self.__height + (self.__offset * 4)
        
        top_left_point = (self.__x_centroid - (dotted_width / 2), self.__y_centroid + (dotted_height / 2))
        top_right_point = (self.__x_centroid + (dotted_width / 2), self.__y_centroid + (dotted_height / 2))
        bottom_left_point = (self.__x_centroid - (dotted_width / 2), self.__y_centroid - (dotted_height / 2))
        bottom_right_point = (self.__x_centroid + (dotted_width / 2), self.__y_centroid - (dotted_height / 2))
        
        return [top_left_point, bottom_left_point, bottom_right_point, top_right_point]

