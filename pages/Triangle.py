import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math

st.title("Geometry")

def guess_triangle(a,b,c):
    if not (a + b > c and a + c > b and b + c > a):
        st.write("Not a triangle")
    else:
        if a > 0 and b > 0 and c > 0:    
            if a == b and b == c and c == a:
                st.write("Equilateral")
                return "Equilateral"
            elif a == b or b == c or c== a:
                st.write("Isoceles")
                return ""
            elif (a**2) + (b**2) == (c**2) or (a**2) + (c**2) == (b**2) or (b**2) + (c**2) == (a**2):
                st.write("Right angle")
                return "Isoceles"
            else:
                st.write("Scalene")
                return "Scalene"
        else:
            st.write("Value cannot be less or equal to zero")
            return "Home"

def draw_triangle(a, b, c, triangle_type):
    plt.figure(figsize=(5, 5))
    if triangle_type == "none":
        st.write("Unable to draw the triangle.")
        return

    if triangle_type == "equilateral":
        points = np.array([[0, 0], [a, 0], [a/2, (np.sqrt(3)/2) * a]])
    elif triangle_type == "isosceles":
        if a == b:
            points = np.array([[0, 0], [c, 0], [c / 2, np.sqrt(a**2 - (c / 2)**2)]])
        elif b == c:
            points = np.array([[0, 0], [a, 0], [a / 2, np.sqrt(b**2 - (a / 2)**2)]])
        else:
            points = np.array([[0, 0], [b, 0], [b / 2, np.sqrt(c**2 - (b / 2)**2)]])
    elif triangle_type == "right-angle":
        points = np.array([[0, 0], [a, 0], [0, b]])
    else:  # scalene
        points = np.array([[0, 0], [a, 0], [b * np.cos(np.arccos((a**2 + b**2 - c**2) / (2 * a * b))), b * np.sin(np.arccos((a**2 + b**2 - c**2) / (2 * a * b)))]])

    plt.plot([points[0][0], points[1][0]], [points[0][1], points[1][1]], 'k-')
    plt.plot([points[1][0], points[2][0]], [points[1][1], points[2][1]], 'k-')
    plt.plot([points[2][0], points[0][0]], [points[2][1], points[0][1]], 'k-')
    plt.fill(points[:, 0], points[:, 1], color="skyblue", alpha=0.5)
    plt.axis("equal")
    plt.axis("off")
    st.pyplot(plt)
    
    
    
    
    #perimeterof triangle
    peri = a + b + c
    st.write(f'Perimeter: {peri}')
    
    s = peri/2
    
    A = math.sqrt(s*((s-a)*(s-b)*(s-c)))
    st.write(f'Area: {A:.2f} square')
          
        
        
        
with st.container(border = True):
    st.write("This is the parent container")

    with st.container(border = True):
        st.write("This is the child container")
        
        with st.container(border = True):
            st.write("This is the grandchild container")
                        
            c1, c2, c3 = st.columns(3)
            with c1:
                st.write("Column 1")        

            with c2:            
                st.write("Column 2")    

            with c3:
                st.write("Column 3")
                
        with st.container(border = True):
            st.write("This is the grandchild container")

c1, c2, c3 = st.columns(3)
with c1:
    with st.container(border = True):
        st.write("Triangle input")
        a = st.number_input("A side")
        b = st.number_input("B side")
        c = st.number_input("C side")
        
        triangle_type = guess_triangle(a,b,c)
        
with c2:
    with st.container(border = True):
        st.write("Triangle picture")
        draw_triangle(a,b,c, triangle_type)
    
#guess_triangle(3,2,4)