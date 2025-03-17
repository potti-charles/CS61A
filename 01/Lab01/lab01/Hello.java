public class Hello{
    static int count = 0;
    public Hello(){ // 构造方法
        count++;
    }
    public void display(){
        System.out.println("对象数量：" + count);}
    public void display2(){
        System.out.println("age：" + count);
    }
    public static void main(String[] args){
        System.out.println("Hello World");
        int x = 10; // 局部变量，必须初始化
        System.out.println("局部变量 x：" + x);
        Hello obj1 = new Hello();
        obj1.display();
        obj1.display2();
        Hello obj2 = new Hello(); // 创建第二个对象
        obj2.display();
        obj2.display2();
    }
}