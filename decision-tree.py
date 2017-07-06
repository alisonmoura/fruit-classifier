from sklearn import tree

# [color, weight, ph]
datas = [
    [1, 150, 5], [1, 140, 5], [1, 135, 5], [1, 120, 5], [1, 145, 5], [1, 160, 5],           #Apple
    [5, 200, 3], [5, 230, 3], [5, 250, 3], [5, 240, 3], [5, 260, 3], [5, 270, 3],           #Orange
    [4, 90, 4.6], [4, 98, 4.6], [4, 95, 4.6], [4, 85, 4.6], [4, 80, 4.6], [4, 100, 4.6],    #Banana
    [6, 60, 4], [6, 88, 4], [6, 75, 4], [6, 66, 4], [6, 80, 4], [6, 65, 4],                 #Grape
    [1, 150, 4], [1, 140, 4], [1, 175, 4], [1, 180, 4], [1, 165, 4], [1, 160, 4],           #Tomato
]
labels = [
    0, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 1, 1,
    2, 2, 2, 2, 2, 2,
    3, 3, 3, 3, 3, 3,
    4, 4, 4, 4, 4, 4,
]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(datas, labels)

def color_to_number(color):
    return {
        "red": 1,
        "blue": 2,
        "green": 3,
        "yellow": 4,
        "orange": 5,
        "purple": 6
    }.get(color, 0)

def get_fruit_name(number):
    return {
        0:"Apple",
        1:"Orange",
        2:"Banana",
        3:"Grape",
        4:"Tomato"
    }.get(number, 'Unknow')

print("================== Welcome to fruits classifier! ==================")
print("Tell me some attributes of a fruit you are thinking now! I wanna guess what it is.")
color = input("Tell me its color (red, blue, green, yellow, purple or orange): ")
weight = input("Tell me its weight (g): ")
ph = input("Tell me its PH: ")
color = color_to_number(color)

if color <= 0:
    print("Please, choose one of this colors (exactly): red, blue, green, yellow, purple or orange");
    exit(1)

predict = clf.predict([[color, weight, ph]])
print(predict[0])
print("The fruit that you are thinking is: " + get_fruit_name(predict[0]))