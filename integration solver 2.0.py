from tkinter import Tk,Frame,Label,Button,Entry,Scale,Listbox,Scrollbar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import figure,plot,axhline,axvline,cla
from matplotlib import use
from math import *

def f():
    pass

def Quit():
    root.destroy()
    try:
        rootA.destroy()
    except:
        pass
    try:
        rootB.destroy()
    except:
        pass

def reset():
    global plot_widget
    function_entry.delete(0,'end')
    lower_entry.delete(0,'end')
    upper_entry.delete(0,'end')
    ans_label.config(text='')
    Dx.set(0.0005)
    cla()
    axhline(0)
    axvline(0)
    plot([],[])
    fig.canvas.draw()
    



def instruction():
    global rootB
    
    rootB=Tk()
    rootB.geometry('480x300+400+100')

    rootB.title('Instructions')
    
    w=Listbox(rootB,bg=theme[0])
    s='''
    Integration Solver v2.0 is mathematical tool capable of
    solving any integration. Input functions are given in the
    programming format. Note eact zeroes are not given instead
    a value very close to zero is given.
    
    sin x -> sin(x)
    [x]+1 -> ceil(x)
     |x|  -> abs(x)
     [x]  -> floor(x)
    ln x  -> log(x)
    log10x-> log10(x)
    x^5   -> x**5
    

    This is a beta version so user might face bugs in the game.
    Developments are still going on.
    Recommendations is gladly accepted.

    Tamojit Das
    IEM CSE
    '''
    s=s.split('\n')
    for c in range(len(s)):
        w.insert(c+1,s[c])
    #w.pack(expand='yes',fill='both')
    w.pack(fill='both',expand='yes')

    

    rootB.mainloop()


def history():
    global rootC
    
    rootC=Tk()
    rootC.geometry('480x300+400+100')
    rootC.title('History')

    
    
    w=Listbox(rootC,bg=theme[0])
    try:
        f=open('history.dat','r')
        s=f.read()
        f.close()
    except:
        f=open('history.dat','w')
        f.close()
        s=''
    s=s.split('\n')
    for c in range(len(s)):
        w.insert(c+1,s[c])
    #w.pack(expand='yes',fill='both')
    w.pack(fill='both',expand='yes')



    rootC.mainloop()

def integrate():
    #try:

    f=lambda x: eval(function_entry.get())
    l=eval(lower_entry.get())
    u=eval(upper_entry.get())
    dx=Dx.get()
    #except:
        #ans_label.config(text='>>> Error !')
        
    ans=0.0
    flag=0
    X=[]
    Y=[]
    c=0.0
    if l>u:
        u,l=l,u
        flag=1
    while l<=u:
        
        try:
            y=f(l)
            p=y*dx
            X.append(l)
            Y.append(y)
            ans+=p
            
        except:
            pass
        l+=dx
    #print(X)
    #print(Y)
    if flag: ans=ans*-1
    cla()
    axhline(0)
    axvline(0)
    plot([],[])
    fig.canvas.draw()


    plot(X,Y)
    fig.canvas.draw()
    ans_label.config(text='= '+str(ans))
    f=open('history.dat','a')
    f.write('\n'+str(function_entry.get())+'\n'+'Lower: '+str(lower_entry.get())+'\n'+'Upper: '+str(upper_entry.get())+'\n'+'= '+str(ans)+'\n')
    f.close()



theme=('orange','blue')

root=Tk()
root.geometry('1600x900')
root.title('Integration Solver v2.0')
root.resizable(0,0)
root.state('zoomed')
root.overrideredirect(True)

Frame(root,width=1600,height=100,bg=theme[1]).place(x=0,y=0)
Label(root,text='Integration Solver',font=('Algerian','26','bold'),bg=theme[1],fg='white').place(x=20,y=20)
Label(root,text='v 2.0',font=('Algerian','18','bold'),bg=theme[1],fg='white').place(x=1280,y=65)

Button(root,text='Instruction',relief='groove',command=instruction,width=8).place(x=20,y=100)
Button(root,text='History',relief='groove',command=history,width=8).place(x=100,y=100)
Button(root,text='Quit',relief='groove',command=Quit,width=8).place(x=1300,y=5)
Label(root,text='@ TD').place(x=1300,y=103)


Frame(root,width=1600,height=700,bg=theme[0]).place(x=0,y=125)

Label(root,text='S',font=('Berlin Sans FB Demi','100','bold'),bg=theme[0],fg=theme[1]).place(x=50,y=150)
Label(root,text='f(x) = ',font=('Berlin Sans FB Demi','36','bold'),bg=theme[0],fg=theme[1]).place(x=130,y=200)

function_entry=Entry(root,width=20,font=('Arial',20))
function_entry.place(x=260,y=215)

upper_entry=Entry(root,width=4,font=('Arial',15))
upper_entry.place(x=60,y=148)

lower_entry=Entry(root,width=4,font=('Arial',15))
lower_entry.place(x=60,y=290)

Label(root,text='dx',font=('Berlin Sans FB Demi','36','bold'),bg=theme[0],fg=theme[1]).place(x=570,y=200)

ans_label=Label(root,text='',font=('Berlin Sans FB Demi','22','bold'),bg=theme[0],fg=theme[1])
ans_label.place(x=50,y=600)


Dx=Scale(root,bg=theme[0],fg=theme[1],from_=0.001,to=0.00001,resolution=0.00001,orient='horizontal',length=250,relief='groove',label='<== SPEED              ::           ACCURACY ==>',activebackground=theme[0])
Dx.set(0.0005)
Dx.place(x=50,y=450)

Button(root,bg=theme[0],fg=theme[1],text='Reset',command=reset,width=8,relief='groove',activebackground=theme[0]).place(x=380,y=480)

Button(root,bg=theme[0],fg=theme[1],text='Integrate',command=integrate,width=8,relief='groove',activebackground=theme[0]).place(x=480,y=480)


use('TkAgg')
fig=figure(1)
canvas=FigureCanvasTkAgg(fig,master=root)
plot_widget=canvas.get_tk_widget()

#x=[1,2,3]
#y=[4,5,6]

axhline(0)
axvline(0)

#fill_between(x,0,y)

#plot(x,y)

plot([],[])


plot_widget.place(x=700,y=200)

#fig.canvas.draw()



root.mainloop()
