## 1. **Arithmetic Operators (Xisaabeed)**
# Tusaale 
x = 10  
y = 3
print("Ku Dar:", x + y)          # KA Dar: 13
print("Ka Jar:", x - y)       # Ka Jar: 7
print("Isku dhufashada:", x * y)  # Isku dhufashada: 30
print("Qaybinta:", x / y)        # Qaybinta: 3.3333333333333335
print("Qaybinta oo dhan:", x // y) # Qaybinta oo dhan: 3
print("Haraaga:", x % y)         # Haraaga: 1
print("Kor u qaadista:", x ** y)  # Kor u qaadista: 1000


## 2. **Assignment Operators (Qaybinta)**
# Tusaale 
x = 5
x += 3  # x = x + 3
print("Ku Dar oo Qaybi:", x)  # Ku Dar oo Qaybi: 8


x *= 2  # x = x * 2  
print("Isku Dhufasho oo Qaybi:", x)  # Isku Dhufasho oo Qaybi: 16

x -= 4  # x = x - 4
print("Ka Jar oo Qaybi:", x)  # Ka Jar oo Qaybi: 12

x /= 3  # x = x / 3
print("Qaybi oo Qaybi:", x)  # Qaybi oo Qaybi: 4.0

x %= 3  # x = x % 3
print("Haraaga oo Qaybi:", x)  # Haraaga oo Qaybi: 1.0



## 3. **Comparison Operators (Isbarbardhig)**
# Tusaale 
a = 10 
b = 20
print("a waa weyn yahay b:", a > b)   # a waa weyn yahay b: False
print("a waa yar yahay b:", a < b)    # a waa yar yahay b: True
print("a waa weyn yahay ama la mid yahay b:", a >= b)  # a waa weyn yahay ama la mid yahay b: False
print("a waa yar yahay ama la mid yahay b:", a <= b)   # a waa yar yahay ama la mid yahay b: True
print("a waa la mid yahay b:", a == b)  # a waa la mid  yahay b: False
print("a waa ka duwan yahay b:", a != b) # a waa ka duwan yahay b: True 


## 4. **Logical Operators (Macquul)**
# Tusaale 
x = True    
y = False
print("x AND y:", x and y)  # x AND y: False
print("x OR y:", x or y)    # x OR y: True
print("NOT x:", not x)       # NOT x: False
print("NOT y:", not y)       # NOT y: True  

## 5. **Membership Operators (Xubin)**
# Tusaale 
my_list = [1, 2, 3, 4, 5]   
print("3 waa ku jiraa liiska:", 3 in my_list)    # 3 waa ku jiraa liiska: True
print("6 ma ku jiraa liiska:", 6 not in my_list)  # 6 ma ku jiraa liiska: True
print("1 waa ku jiraa liiska:", 1 in my_list)    # 1 waa ku jiraa liiska: True
print("7 ma ku jiraa liiska:", 7 not in my_list)  # 7 ma ku jiraa liiska: True
