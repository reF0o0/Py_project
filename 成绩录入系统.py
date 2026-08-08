# print("输入成绩，判断是否及格")
# grade = float(input("请输入你的成绩："))
# if grade >= 60:
#     print("及格")
# else:
#     print("不及格")

# stu = { }
# name = input("请输入你的名字：")
# age = int(input("请输入你的年龄："))
# stu[name] = age
# print(stu)

# def add_student(students,name,age):
#     students[name] = int(age)

# def show_student(students):
#     for name,age in students.items( ):
#         print(f"{name}的年龄是{age}")

# students = { }
# while True:
#     print("按'q'退出")
#     name = input("请输入姓名：")
#     if name == "q":
#         break
#     else:
#         age = input("请输入年龄：")
#         add_student(students,name,age)
# show_student(students)

#成绩记录系统
def add_student(students,name,subject,mark):
    if name not in students:
        students[name] = {subject:int(mark)}
    else:
        students[name][subject] = int(mark)

def show_students(students):
    for name,scores in students.items( ):
        for subject,mark in scores.items( ):
            print(name,subject,mark)
        avg = sum(scores.values( ))/len(scores)
        print(f"{name} 平均分：{avg}")

def main( ):
    students = { }
    while True:
        print("欢迎使用学生成绩录入系统")
        print("1  添加学生成绩\n2  查询所有成绩\n'q'退出")
        option = input("输入内容：")
        if option in ("1","2","q"):
            if option == "1":
                name = input("学生姓名：")
                subject = input("学科：")
                while True:
                    mark = input("分数：")
                    if mark.isdigit( ) and 0 <= int(mark) <= 100:
                        break
                    else:
                        print("请输入0~100的数字")
                add_student(students,name,subject,mark)
            elif option == "2":
                if students:
                    show_students(students)
                else:
                    print("目前还没有学生信息")
            else:
                print("成功退出")
                break
        else:
            print("输入错误")

if __name__ == "__main__":
    main( )