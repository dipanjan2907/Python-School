print("1.Find Area \n2.Find Perimeter")
c1=int(input("Enter your choice: "))
print("1.Square \n2.Rectangle \n3.Circle \n4.Triangle")
c2=int(input("Enter your choice: "))
match c1:
    case 1:        
        match c2:
            case 1:
                s=int(input("Enter side of square: "))
                print("Area of square: ",s*s)
            case 2:
                l=int(input("Enter length of rectangle: "))
                b=int(input("Enter breadth of rectangle: "))
                print("Area of rectangle: ",l*b)
            case 3:
                r=int(input("Enter radius of circle: "))
                print("Area of circle: ",3.14*pow(r,2))
            case 4:
                s1=int(input("Enter first side of triangle: "))
                s2=int(input("Enter second side of triangle: "))
                s3=int(input("Enter third side of triangle: "))
                s=(s1+s2+s3)/2
                print("Area of Triangle: ",(s*(s-s1)*(s-s2)*(s-s3))**0.5)
    case 2:
        match c2:
            case 1:
                s=int(input("Enter side of square: "))
                print("Perimeter of square: ",4*s)
            case 2:
                l=int(input("Enter length of rectangle: "))
                b=int(input("Enter breadth of rectangle: "))
                print("Perimeter of rectangle: ",2*(l*b))
            case 3:
                r=int(input("Enter radius of circle: "))
                print("Perimeter of circle: ",2*3.14*r)
            case 4:
                s1=int(input("Enter first side of triangle: "))
                s2=int(input("Enter second side of triangle: "))
                s3=int(input("Enter third side of triangle: "))
                print("Perimeter of triangle: ",s1+s2+s3)
        
