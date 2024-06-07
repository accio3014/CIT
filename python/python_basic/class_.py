# class_.py

class FourCal :
    def setdata(self, first, second):   # class 내부에 있는 function을 method라고 부름, method를 만들때 무조건 self가 처음에 들어가야 함
        self.first = first
        self.second = second

a = FourCal()       # a는 object, FourCal 클래스의 instance는 a
a.setdata(3, 7)     # self에는 값을 넘겨주는 것이 X