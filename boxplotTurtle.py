import turtle

class Boxplot:
    def rectfill(self,t,h,w,c):
        t.fillcolor(c)
        t.begin_fill()
        for i in range(2):
            t.forward(w)
            t.right(90)
            t.forward(h)
            t.right(90)
        t.end_fill()
        t.forward(w)
        t.right(90)
        t.forward(h/2)
        t.left(90)
        
    def plot_graph(self,t):
        t.penup()
        t.goto(t.pos()+(-230,-60))
        t.pendown()
        self.arrow(t)
        t.forward(450)
        t.right(180)
        self.arrow(t)      

    def arrow(self,t):
        t.left(30)
        t.forward(10)
        t.backward(10)
        t.right(60)
        t.forward(10)
        t.backward(10)
        t.left(30)
        
    def sketch(self):
        s=turtle.Screen()
        s.setup(500,200)
        t=turtle.Turtle()
        self.boxplot()
        t.pensize(3)
        self.plot_graph(t)
        t.pensize(1)
        self.marking(t,self.mi,self.d)
        t.right(90)
        t.penup()
        t.forward(60)
        t.pendown()
        t.forward(40)
        t.write(self.mi)
        t.backward(20)
        t.right(90)
        t.forward(50*(self.Q1-self.mi)/self.d)
        t.left(90)
        t.forward(40)
        t.right(90)
        t.write(self.Q1)
        w1=(50*(self.Q2-self.Q1)/self.d)
        self.rectfill(t,80,w1,'red')
        t.left(90)
        t.forward(40)
        t.right(90)
        t.write(self.Q2)
        w2=(50*(self.Q3-self.Q2)/self.d)
        self.rectfill(t,80,w2,'green')
        t.left(90)
        t.forward(40)
        t.write(self.Q3)
        t.backward(40)
        t.right(90)
        t.forward(50*(self.mx-self.Q3)/self.d)
        t.left(90)
        t.forward(20)
        t.write(self.mx)
        t.backward(40)
        t.forward(20)
        t.right(90)
        t.penup()
        t.forward(20)
        turtle.Screen().exitonclick()
        

    def marking(self,t,s,f):
        for i in range(8):
            t.forward(50)
            t.left(90)
            t.forward(5)
            t.penup()
            t.forward(15)
            t.write(s+f*(7-i))
            t.backward(15)
            t.pendown()
            t.backward(10)
            t.forward(5)
            t.right(90)

    def boxplot(self):
        print("Horizontal BoxPlot".center(50,'*'))
        n=input("Enter the DataSet Values Separated by Spaces:\n")
        ds=list(map(float,n.rstrip().split(' ')))
        ds=sorted(ds)
        self.mi=ds[0]
        self.mx=ds[len(ds)-1]
        self.d=(self.mx-self.mi)//8+1
        if (self.d)*7+self.mi<self.mx:
            self.d=self.d+1
        if len(ds)%2==0:
            self.Q1=self.med(ds[:len(ds)//2])
            self.Q2=self.med(ds)
            self.Q3=self.med(ds[len(ds)//2:])
        else:
            self.Q1=self.med(ds[:len(ds)//2])
            self.Q2=self.med(ds)
            self.Q3=self.med(ds[len(ds)//2+1:])
            
        #All Values
        print("DS:",ds,"\nMIN:",self.mi,"\nQ1:",self.Q1,"\nQ2:",self.Q2,"\nQ3:",self.Q3,"\nMAX:",self.mx)

    def med(self,ds):
        n=len(ds)//2
        if(len(ds)%2==0):
            return (ds[n]+ds[n-1])/2
        else:
            return ds[n]
               
b = Boxplot()
b.sketch()




