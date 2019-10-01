import java.util.*;

class Student
{
	int reg;
	String name;
	int age;

	void setData(int r, String n, int a)
	{
		reg = r;
		name = n;
		age = a;
	}
	void display()
	{
		System.out.println(reg+" "+name+" "+age);
	}
}

class Demo
{
	public static void main(String args[])
	{
		
		int j,i=0;
		int l = args.length;
		int objects = l/3;
		Student s[] = new Student[objects];
		
		for(j=0;j<objects;j++)
		{
			s[j] = new Student();
			int x = Integer.parseInt(args[i]);
			int y = Integer.parseInt(args[i+2]);
			s[j].setData(x,args[i+1],y);
			s[j].display();
			i+=3;
			
		}
	}
}
		
