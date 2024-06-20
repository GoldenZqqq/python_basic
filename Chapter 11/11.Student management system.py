"""
需求：学生管理系统

学生

老师

班级

课程


"""


class User(object):
    # 属性：姓名、年龄、性别、学(工)号
    def __init__(self, name, age, gender, id):
        self.name = name
        self.age = age
        self.gender = gender
        self.id = id

    def show_info(self):
        print("*" * 30)
        print(f"姓名：{self.name}")
        print(f"年龄：{self.age}")
        print(f"性别：{self.gender}")
        print(f"学(工)号：{self.id}")
        print("*" * 30)


class Student(User):
    # 属性：姓名、年龄、性别、学号
    def __init__(self, name, age, gender, id):
        super().__init__(name, age, gender, id)
        self.courseList = []

    def show_info(self):  # 显示学生信息
        super().show_info()
        if self.courseList:
            print("该学生的选课信息：")
            for i in self.courseList:
                print(i.name)
        else:
            print("该学生还未选课")
        print("*" * 11 + "学生信息" + "*" * 11)

    def add_course(self, course):
        self.courseList.append(course)


class Teacher(User):
    # 属性：姓名、年龄、性别、工号、是否是导员、班级列表
    def __init__(self, name, age, gender, id, isDirector, classList):
        super().__init__(name, age, gender, id)
        self.isDirector = isDirector
        self.classList = classList

    def show_info(self):
        super().show_info()
        print("是否是辅导员：%s" % ["否", "是"][self.isDirector])
        if not self.classList:
            print("辅导班级：无")
        else:
            print("辅导班级：")
            for i in self.classList:
                print(i)
        print("*" * 30)


class Class(object):  # 班级
    # 属性：班级名称、班级号、辅导员、学生
    def __init__(self, name, id, teacher, studentList):
        self.name = name
        self.id = id
        self.teacher = teacher
        self.studentList = studentList

    def show_info(self):
        print("*" * 11 + "班级信息" + "*" * 11)
        print("班级名称：%s" % self.name)
        print("班级号：%s" % self.id)
        print("辅导员：%s" % self.teacher.name)
        if not self.studentList:
            print("学生信息：无")
        else:
            print("学生信息：")
            for i in self.studentList:
                print(i.name)
        print("*" * 30)

    def add_student(self, student):  # 增加学生
        if student in self.studentList:
            raise Exception("该学生已经在该班级！")
        else:
            self.studentList.append(student)
            return True

    def sub_student(self, student):  # 删除学生
        if student in self.studentList:
            self.studentList.remove(student)
            return True
        else:
            raise Exception("该学生不在该班级！")


class Course(object):  # 课程
    # 属性：课程名称、课程号、教师、学生列表、课程性质、课程容量
    allCourseList = []  # 类属性

    def __init__(self, name, id, teacher, studentList, type, capacity):
        self._name = name
        self.id = id
        self.teacher = teacher
        self.studentList = studentList
        self.type = type
        self.capacity = capacity
        self.student_number = len(self.studentList)
        self.remain_number = self.capacity - self.student_number
        Course.allCourseList.append(self.name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name == "":
            raise Exception("课程名称不能为空！")
        if not isinstance(name, str):
            raise Exception("课程名称必须为字符串！")
        self._name = name

    def show_info(self):
        print("*" * 11 + "课程信息" + "*" * 11)
        print("课程名称：%s" % self.name)
        print("课程号：%s" % self.id)
        print("教师：%s" % self.teacher.name)
        print("课程性质：%s" % self.type)
        print("课程容量：%d人" % self.capacity)
        print("已选学生人数：%d人" % self.student_number)
        print("剩余学生空位：%d人" % self.remain_number)
        if not self.studentList:
            print("学生信息：无")
        else:
            print("学生信息：")
            for i in self.studentList:
                print(i.name)
        print("*" * 30)

    def add_student(self, student):  # 增加学生
        if student in self.studentList:
            raise Exception("该学生已经在该课程！")
        elif self.remain_number <= 0:
            raise Exception("该课程已满，请选择其他课程！")
        else:
            self.studentList.append(student)
            self.student_number += 1
            self.remain_number -= 1
            student.add_course(self)
            return True

    def remove_student(self, student):  # 删除学生
        if student in self.studentList:
            self.studentList.remove(student)
            self.student_number -= 1
            self.remain_number += 1
            return True
        else:
            raise Exception("该学生不在该课程！")

    @classmethod
    def show_all_course(cls):  # 显示所有课程
        print("*" * 9 + "所有课程信息" + "*" * 9)
        for i in cls.allCourseList:
            print(i)
        print("*" * 30)


# 创建学生对象
mia = User("mia", 19, "女", 1)
rose = Student("rose", 20, "女", 2)
lily = Student("lily", 18, "女", 3)
# 创建教师对象
jack = Teacher("jack", 50, "男", 5, False, [])
tom = Teacher("tom", 26, "男", 53, True, ["计算机二班", "法律3班"])
# 创建班级对象
computer_2 = Class("计算机二班", 1002, tom, [])
computer_1 = Class("计算机一班", 1001, tom, [mia])
# 创建课程对象
python = Course("python", 1, jack, [mia, rose], "必修课", 6)
java = Course("java", 2, tom, [mia, rose, lily], "选修课", 4)
python.add_student(lily)
python.remove_student(mia)
python.show_info()
print(Course.show_all_course())
python.name = "Python精讲"
print(python.name)
