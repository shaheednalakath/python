from graphics import circle,rectangle

from graphics.packages import cuboid,sphere
r=int(input("enter a radius"))
print(circle.area(r))
w=int(input("enter width"))
l=int(input("enter length"))
print(rectangle.area_rect(w,l))
print(cuboid.cub_area(r,r,r))

