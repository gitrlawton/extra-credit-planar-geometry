# PROGRAMMER: Ryan Lawton

# IMPORT STATEMENTS






class InsideCircle:

# CONSTRUCTOR
    
    def __init__(self, radius, offset, x_centroid, y_centroid):
        if type(radius) is not float:
            raise TypeError(
                "InsideCircle.py __init__ radius - must be a float."
            )
        if radius <= 0:
            raise ValueError(
                "InsideCircle.py __init__ radius - must be greater than 0."
            )
        if type(offset) is not float:
            raise TypeError(
                "InsideCircle.py __init__ offset - must be a float."
            )
        if offset <= 0:
            raise ValueError(
                "InsideCircle __init__ offset - must be greater than 0."
            )
        if type(x_centroid) is not float:
            raise TypeError(
                "InsideCircle.py __init__ x_centroid - must be a float."
            )
        if type(y_centroid) is not float:
            raise TypeError(
                "InsideCircle.py __init__ y_centroid - must be a float."
            ) 
        
        self.__radius = radius
        self.__offset = offset
        self.__x_centroid = x_centroid
        self.__y_centroid = y_centroid

# INSTANCE METHODS
    
    def get_radius(self):
        return self.__radius
    
    def get_offset(self):
        return self.__offset
    
    def get_x_centroid(self):
        return self.__x_centroid
    
    def get_y_centroid(self):
        return self.__y_centroid
    
    def circle_points_clockwise(self):
        top_point = (self.__x_centroid, self.__y_centroid + self.__radius)
        bottom_point = (self.__x_centroid, self.__y_centroid - self.__radius)
        left_point = (self.__x_centroid - self.__radius, self.__y_centroid)
        right_point = (self.__x_centroid + self.__radius, self.__y_centroid)
        
        return [top_point, right_point, bottom_point, left_point]
    
    def circle_points_counterclockwise(self):
        top_point = (self.__x_centroid, self.__y_centroid + self.__radius)
        bottom_point = (self.__x_centroid, self.__y_centroid - self.__radius)
        left_point = (self.__x_centroid - self.__radius, self.__y_centroid)
        right_point = (self.__x_centroid + self.__radius, self.__y_centroid)
        
        return [top_point, left_point, bottom_point, right_point]
    
    def dashed_circle_points_clockwise(self):
        top_point = (self.__x_centroid, self.__y_centroid + self.__radius + self.__offset)
        bottom_point = (self.__x_centroid, self.__y_centroid - self.__radius - self.__offset)
        left_point = (self.__x_centroid - self.__radius - self.__offset, self.__y_centroid)
        right_point = (self.__x_centroid + self.__radius + self.__offset, self.__y_centroid)
        
        return [top_point, right_point, bottom_point, left_point]
    
    def dashed_circle_points_counterclockwise(self):
        top_point = (self.__x_centroid, self.__y_centroid + self.__radius + self.__offset)
        bottom_point = (self.__x_centroid, self.__y_centroid - self.__radius - self.__offset)
        left_point = (self.__x_centroid - self.__radius - self.__offset, self.__y_centroid)
        right_point = (self.__x_centroid + self.__radius + self.__offset, self.__y_centroid)
        
        return [top_point, left_point, bottom_point, right_point]
    
    def dotted_circle_points_clockwise(self):
        top_point = (self.__x_centroid, self.__y_centroid + self.__radius + (self.__offset * 2))
        bottom_point = (self.__x_centroid, self.__y_centroid - self.__radius - (self.__offset * 2))
        left_point = (self.__x_centroid - self.__radius - (self.__offset * 2), self.__y_centroid)
        right_point = (self.__x_centroid + self.__radius + (self.__offset * 2), self.__y_centroid)
        
        return [top_point, right_point, bottom_point, left_point]
    
    def dotted_circle_points_counterclockwise(self):
        top_point = (self.__x_centroid, self.__y_centroid + self.__radius + (self.__offset * 2))
        bottom_point = (self.__x_centroid, self.__y_centroid - self.__radius - (self.__offset * 2))
        left_point = (self.__x_centroid - self.__radius - (self.__offset * 2), self.__y_centroid)
        right_point = (self.__x_centroid + self.__radius + (self.__offset * 2), self.__y_centroid)
        
        return [top_point, left_point, bottom_point, right_point]
    