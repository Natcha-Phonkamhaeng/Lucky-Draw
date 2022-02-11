'''
Create two app in one program
1. Lucky Draw --> finish
2. Roll a dice

'''

from tkinter import *
import random

class Title:

	def __init__(self, master):
		self.frame = Frame(master, bg='black')
		self.frame.pack(fill='both', expand=True)

		self.lucky_draw_btn = Button(self.frame, text='Lucky Draw', font=font_text(20), bg='light blue', command=self.delete_widget)
		self.lucky_draw_btn.grid(row=1, column=0, pady=150, padx=160)

		self.roll_dice_btn = Button(self.frame, text='Roll A Dice', font=font_text(20), bg='light green')
		self.roll_dice_btn.grid(row=1, column=1)

	def delete_widget(self):
		self.frame.destroy()
		lucky_draw_title = LuckyDraw_Title(root)
		lucky_draw_title.draw()


class LuckyDraw_Title:

	def __init__(self, master):
		self.frame = Frame(master, bg='light blue')
		self.frame.pack(fill='both', expand=True)

		self.welcome_text = Label(self.frame, text='Welcome to Lucky Draw', font=font_text(20) , bg='light blue', fg='magenta')
		self.welcome_text.pack(pady=150)

		self.enter_btn = Button(self.frame, text='Enter', width=20, bg='green', command=self.delete_widget)
		self.enter_btn.place(relx=0.5, rely=0.6, anchor='center')	

	def chg_color_text(self):
		self.current_color = self.welcome_text.cget('fg')
		self.next_color = 'magenta' if self.current_color == 'green' else 'green'
		self.welcome_text.config(fg=self.next_color)
		self.welcome_text.after(1000, self.chg_color_text)

	def chg_color_btn(self):
		self.current_color_btn = self.enter_btn.cget('bg')
		self.next_color_btn = 'green' if self.current_color_btn == 'magenta' else 'magenta'
		self.enter_btn.config(bg=self.next_color_btn)
		self.enter_btn.after(1000, self.chg_color_btn)

	def draw(self):
		self.chg_color_text()
		self.chg_color_btn()

	def delete_widget(self):
		self.frame.destroy()
		lucky_draw = LuckyDraw(root)


class LuckyDraw:

	def __init__(self,master):
		self.frame = Frame(master, bg='light green')
		self.frame.pack(fill='both', expand=True)
	
		self.text_box = Text(self.frame, width=50, height=5)
		self.text_box.pack(pady=15)

		self.enter_draw = Button(self.frame, text='Get The Winner !!', command=self.draw, fg='magenta', font=font_text(15))
		self.enter_draw.pack()

		self.name = Label(self.frame, text='')
		self.num = Label(self.frame, text='')
		self.lucky_winner = Label(self.frame, text='')

	def draw(self):
		self.get_text = self.text_box.get('1.0', 'end-1c').split(',')

		for i in range(len(self.get_text)):
			self.get_text[i] = self.get_text[i].upper().strip()

		self.get_text = set(self.get_text)

		self.name.config(text=f'Name of contestant: {tuple(self.get_text)}', font=font_text(13), bg='light green')
		self.num.config(text=f'Number of contestant is: {len(self.get_text)}', font=font_text(13), bg='light green')
		self.lucky_winner.config(text=f'The winner is: {random.choice(list(self.get_text))}', bg='yellow', font=font_text(15))

		self.num.pack(pady=10)
		self.name.pack(pady=10)
		self.lucky_winner.pack(pady=10)


def font_text(num):
	font_text1 = ('Comic Sans MS', int(num), 'bold')
	return font_text1


root = Tk()
root.title('Lucky Draw')
root.geometry('800x400+2000+150')

title = Title(root)

# delete this line of code if you push to production.
root.bind('<Escape>', lambda x: root.quit())
root.mainloop()
