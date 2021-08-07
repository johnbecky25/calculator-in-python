from tkinter import *
import math

root=Tk()
root.title('calculator')

try:
   def insertion_(num):
        pre=ent.get()
        ent.delete(0,END)
        ent.insert(0,str(pre) + str(num))
    
    
   def addition():
      try:
         global num1
         num1=float(ent.get())
         global sign
         sign="addition"
         ent.delete(0,END)
      except:
         ent.insert(0,"SYNTAX ERROR")
    
    
   def subtraction(): 
       global num1
       try:
          num1=float(ent.get())
          global sign
          sign="subtraction"
          ent.delete(0,END)
       except:
            ent.insert(0,"SYNTAX ERROR")
           
    
   def multiply():
      try:
         global num1
         num1=float(ent.get())
         global sign
         sign="times"
         ent.delete(0,END)
      except:
         ent.insert(0,"SYNTAX ERROR")
    
   def division():
       try:
          global num1
          num1=float(ent.get())
          global sign
          sign="divide"
          ent.delete(0,END)
       except:
          ent.insert(0,"SYNTAX ERROR")
    
   def square():
      try:
         global sign
         sign='sq'
         global num1
         num1=float(ent.get())
         ent.delete(0,END)
      except:
         ent.insert(0,"SYNTAX ERROR")

   def square_root():
      global sign 
      sign='sqrt'
     
   def log():
       global sign 
       sign='logarithm'
       

   def delete():
       length=(ent.get())
       len_=len(length)
       ent.delete(len_-1,END)
    
   def inverse_():
         global num1
         num1=float(ent.get())
         global sign
         sign='inv' 
         ent.delete(0,END)
         
   def cos_():
         global sign
         sign='cos' 
         ent.delete(0,END)
      
   def tan_():
        global sign
        sign='tan' 
        ent.delete(0,END)   

    
   def answer_equals():
       try:
          if sign=='addition':
             num2 = float(ent.get())
             ent.delete(0,END)
             answer=num1+num2
             ent.insert(0, str(answer))
          elif sign=='subtraction':
               num2 = float(ent.get())
               ent.delete(0,END)
               answer=num1-num2
               ent.insert(0,answer)
          elif sign=="times":
               num2 = float(ent.get())
               ent.delete(0,END)
               answer=num1*num2
               ent.insert(0,answer)

          elif sign=="divide":
               num2 = float(ent.get())
               ent.delete(0,END)
               try:
                  answer=float(num1/num2)
                  ent.insert(0,answer)
               except:
                  ent.insert(0,"Math Error")
        
          elif sign=='sq':
               answer=num1*num1
               ent.insert(0,answer)

          elif sign=='sqrt':
               num=float(ent.get())
               answer=float(math.sqrt(num))
               ent.insert(0,answer)
        
          elif sign =='logarithm':
               log_num=float(ent.get())
               answer=(math.log10(log_num))
               ent.insert(0,answer)
              
          elif sign=='inv':
               try:            
                  answer=float(1/num1)
                  ent.insert(0,answer)
               except:
                  ent.insert(0,"MATH ERROR")
           
          elif sign=='tan':
               tan_num=float(ent.get())
               answer=float(math.tan(tan_num))
               ent.insert(0,answer)
           
          elif sign=='cos':
               cos_num=float(ent.get())
               answer=float(math.cos(cos_num)) 
               ent.insert(0,answer)
             
       except Exception as err:
         ent.insert(0,"SYNTAX ERRORS")
         print(err)
         
     
       
       
       
       

   def clear():
       ent.delete(0,END)
except:
    print("Syntax Error")       



  
ent=Entry(bd=2,bg='grey',fg='black',width=35)
ent.grid(row=0,column=0,columnspan=5)

#font=('digital-7', 120)




button9=Button(root,relief='raised',bd=3,text='9',width=4,height=4,command =lambda :insertion_(9))
button9.grid(row=1,column=0)

button8=Button(root,relief='raised',bd=3,text='8',width=4,height=4,command=lambda :insertion_(8))
button8.grid(row=1,column=1)

button7=Button(root,relief='raised',bd=3,text='7',width=4,height=4,command=lambda : insertion_(7))
button7.grid(row=1,column=2)

button6=Button(root,relief='raised',bd=3,text='6',width=4,height=4,command=lambda :insertion_(6))
button6.grid(row=2,column=0)

button5=Button(root,relief='raised',bd=3,text='5',width=4,height=4,command= lambda :insertion_(5))
button5.grid(row=2,column=1)

button4=Button(root,relief='raised',bd=3,text='4',width=4,height=4,command=lambda : insertion_(4))
button4.grid(row=2,column=2)

button3=Button(root,relief='raised',bd=3,text='3',width=4,height=4,command=lambda : insertion_(3))
button3.grid(row=3,column=0)

button2=Button(root,relief='raised',bd=3,text='2',width=4,height=4,command=lambda : insertion_(2))
button2.grid(row=3,column=1)

button1=Button(root,relief='raised',bd=3,text='1',width=4,height=4,command=lambda : insertion_(1))
button1.grid(row=3,column=2)

button_zero=Button(root,relief='raised',bd=5,text='0',width=4,height=4,command=lambda : insertion_(0))
button_zero.grid(row=4,column=0)

button_add=Button(root,relief='raised',width=4,bd=3,text='+',height=4,command=addition)
button_add.grid(row=5,column=1)

button_equals=Button(root,relief='raised',bd=3,width=4,text='=',height=9,fg='white',bg='green',command=answer_equals)
button_equals.grid(row=4,column=4,rowspan=2)

button_clear=Button(root,relief='raised',bd=3,width=4,text='CE',fg='green',height=4,command=clear)
button_clear.grid(row=4,column=1)

button_sub=Button(root,relief='raised',bd=3,width=4,text='-',height=4,fg='green',command=subtraction)
button_sub.grid(row=3,column=3)

button_multiply=Button(root,relief='raised',bd=3,width=4,text='*',height=4,command=multiply)
button_multiply.grid(row=2,column=3)

button_divide=Button(root,relief='raised',bd=3,width=4,text='/',height=4,command=division).grid(row=1,column=3)

button_square=Button(root,relief='raised',bd=3,width=4,text='^2',height=4,command=square).grid(row=2,column=4)

button_sqrt=Button(root,relief='raised',bd=3,width=4,text='sqrt',height=4,command=square_root).grid(row=3,column=4)

button_log=Button(root,relief='raised',bd=3,text='LOG',width=4,height=4,command=log).grid(row=1,column=4)

button_delete =Button(root,relief='raised',bd=3,text='DEL',width=4,fg='red',height=4,command=delete).grid(row=4,column=2)

button_float =Button(root,relief='raised',bd=3,text='.',width=4,height=4,command = lambda :insertion_('.') ).grid(row=5,column=0)

button_inv =Button(root,relief='raised',bd=3,text='inv',width=4,height=4,command =inverse_ ).grid(row=5,column=2)

button_cos =Button(root,relief='raised',bd=3,text='cos',width=4,height=4,command = cos_ ).grid(row=5,column=3)

button_tan =Button(root,relief='raised',bd=3,text='tan',width=4,height=4,command = tan_).grid(row=4,column=3)

root.mainloop()
