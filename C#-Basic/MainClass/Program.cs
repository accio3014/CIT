using System;

class Person {
  // 속성(Property)
  public string Name;
  public string Birthday;
  public string Gender;

  // 메소드(Method)
  public void Eat()
  {
    // 먹는 행위
  }

  public void Walk()
  {
    // 걷는 행위
  }

  public void Run()
  {
    // 뛰는 행위
  }
}

class MainClass {

  public static void Main (string[] args) {

    // bool boolVariable = true;
    // int intVariable = 10;
    // float floatVariable = 3.4f;
    // char charVariable = 'a';

    // Console.WriteLine(boolVariable);
    // Console.WriteLine(intVariable);
    // Console.WriteLine(floatVariable);
    // Console.WriteLine(charVariable);

    // for(int i=1; i<11; i++) {
    //     Console.WriteLine(i);
    // }

    // int j=1;
    // while(j<11) {
    //     Console.WriteLine(j++);
    // }

    int score = 85;

    // 논리 연산자를 사용하지 않은 경우
    if (score > 80) {
        if (score <= 100) {
            Console.WriteLine("A");
        }
    }
      

    // 논리 연산자를 사용한 경우
    if ((score > 80) && (score <= 100)) {
        Console.WriteLine("A");
    }

  }
}
