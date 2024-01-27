
#  Desenvolva um código utilizando seus conhecimentos de Tkinter para converter uma unidade de medida de centímetros para metros.


from tkinter import *

janela = Tk()

janela.title('Conversor de Medida')
janela.geometry('400x250')

medida_Label = Label(text='''Digite uma medida em centimetro,
converterei em metro.''', height= 2, font=('Arial', 15) )
medida_Label.pack()
medida_Input = Entry()
medida_Input.pack()

def converter():
    medidaEmCM = int(medida_Input.get())

    if medidaEmCM < 0:
        resultado_Label.configure(text='''Apenas números positivos, 
        não existe altura negativa.''', font=('Arial', 15))
        medida_Input.delete(0, END)
        medida_Input.focus()
    else:
        medidaEmMetro = medidaEmCM/100
        resultado_Label.configure(text=f'''A medida que você ofereceu ({medidaEmCM}cm),
        convertida em metro é: {medidaEmMetro}m.''', font=('Arial', 15))

        medida_Input.delete(0, END)
        medida_Input.focus()

botao = Button(janela, text='Converter', command=converter, height=2, font=('Arial', 15) )
botao.pack()

resultado_Label = Label(text='')
resultado_Label.pack()




janela.mainloop()