class Standard:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = int(chinese)
        self.math = int(math)
        self.english = int(english)

    @property
    def average(self):
        return (self.chinese + self.math + self.english) / 3

    @property
    def total(self):
        return self.chinese + self.math + self.english


class Student(Standard):
    pass


def add_student():
    while True:
        name = input("请输入学生姓名：")
        if name in students:
            print("该学生已存在；如需更改，请先删除。")
            continue

        else:
            break

    while True:
        chinese = input("请输入学生语文成绩：")
        if chinese.isdigit() and int(chinese) in range(0, 101):
            break
        else:
            print("只能输入0～100的数字")

    while True:
        math = input("请输入学生数学成绩：")
        if math.isdigit() and int(math) in range(0, 101):
            break
        else:
            print("只能输入0～100的数字")

    while True:
        english = input("请输入学生英语成绩：")
        if english.isdigit() and int(english) in range(0, 101):
            break
        else:
            print("只能输入0～100的数字")

    stu = Student(name, chinese, math, english)
    students[stu.name] = stu
    print("添加成功")


def get_total(x):
    return x.total


students = {}

while True:
    print("""欢迎使用学生成绩管理系统
    请选择您的服务
    1  添加学生（姓名、语文、数学、英语）
    2  删除学生
    3  查看所有学生
    4  查询某学生总分/平均分
    5  按总分排序
    按 q 退出
    """)
    while True:
        option = input("请输入：")
        if option not in ("1", "2", "3", "4", "5", "q"):
            print("输入错误")

        else:
            break

    if option == "1":
        add_student()

    elif option == "2":
        while True:
            del_name = input("您要删除的学生姓名：(按 q 退出)")
            if del_name in students:
                del students[del_name]
                break

            elif del_name == "q":
                break

            else:
                print("没有这个学生，请重新输入")

    elif option == "3":
        for name, stu in students.items():
            print(
                f"{name}的语文成绩：{stu.chinese}，数学成绩：{stu.math}，英语成绩：{stu.english}"
            )

    elif option == "4":
        while True:
            sch_name = input("您要查询的学生姓名：(按 q 退出)")
            stu = students.get(sch_name)
            if stu is None and sch_name != "q":
                print("还没有这个学生")
                continue

            elif stu:
                print(f"{sch_name}的平均分：{stu.average}，总分：{stu.total}")

            else:
                break

    elif option == "5":
        if students:
            rank = sorted(students.values(), key=get_total, reverse=True)
            for stu in rank:
                print(f"{stu.name}的总分是：{stu.total}")
        else:
            print("还没有学生")

    else:
        break
