class Shape:
    def area(self):
        """
        This method is intended to be overridden in subclasses.
        If a subclass doesn't implement it but it is called, NotImplemented will be raised.
        """
        raise NotImplemented

        @abstractmethod
        def perimeter(self):
            pass






class Rectangle(Shape): # Super class
      """A Super class."""    # docstring
      Methods = list() # class public attribute
      def __init__(self, w, h):   # Constructor with two params
        self.__width = w # instance private attribute
        self.__height = h # instance private attribute
        print("Rectangle object with (width : ",self.width," , height : ",self.height,") is Initialized")

      def __del__(self):    # Destructor
        print("Rectangle object with (width : ",self.width," , height : ",self.height,") is Destructed")

      def area(self): # class method
        return self.width * self.height

      def perimeter(self): # class method
        return 2 * (self.width + self.width)

      # property
      @property
      def width(self): # getter
          return self.__width
      @width.setter
      def width(self,width): # setter
          self.__width = width

      @property
      def height(self): # getter
         return self.__height
      @height.setter
      def height(self, height): # setter
         self.__height = height




class Square(Rectangle): # Sub class(Square) inherit from super class(Rectangle)
      """A Sub class of Rectangle """  # docstring
      def __init__(self, s): # Constructor with one param
        # call parent constructor, w and h are both s
        super(Square, self).__init__(s, s) #call parent constructor
        self._s = s # instance protect attribute

      def __del__(self): # overridden  Destructor
        print("Square object with ( height : ",self._s,") is Destructed")


      """ Square objects will inherts  Rectangle Methods and attributes:
      - Methods = list()
      - self.width = s
      - self.height = s
      - def area(self):
      - def perimeter(self):
      
      """





def main():
    Rect = Rectangle(10,20)  # object of class Rectangle
    print("Rect object area = ",Rect.area()) # call of Rectangle area() class method
    print("Rect object perimeter =",Rect.perimeter()) # call of Rectangle perimeter() class method
    Squ = Square(10)
    print("Squ object area = ",Squ.area()) # call of Square inherted area() class method
    print("Squ object perimeter =",Squ.perimeter()) # call of Square inherted perimeter() class method






if __name__ == '__main__':
    main()




