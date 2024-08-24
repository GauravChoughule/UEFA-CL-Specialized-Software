
from random import shuffle
from tkinter import *

teams = ['Arsenal', 'Aston Villa', 'Liverpool', 'Man City',
         'Atlético de Madrid', 'Girona', 'Real Madrid',
         'Bayern Munich', 'Dortmund', 'Leipzig', 'Leverkusen', 'Stuttgart',
         'Atalanta', 'Bologna', 'Inter', 'Juventus', 'Milan',
         'Brest', 'Monaco', 'Paris Saint-Germain',
         'Feyenoord', 'PSV Eindhoven', 'Benfica', 'Sporting CP', 'Club Brugge', 'Celtic', 'Sturm Graz', 'Shakhtar Donetsk']

shuffle(teams)
size = len(teams)

root = Tk()
root.geometry('1370x700+0+0')
root.title('UEFA Specialized Software')

header = Frame(root, width=1370, bd=4)
header.pack(side=TOP, fill=X)
Label(header, text='"SPECIALIZED SOFTWARE" for UEFA', font=('Times New Roman', 36, 'bold'), fg='cyan', bg='blue', bd=6, relief='ridge').pack(side=TOP, fill=X)

def predictions():
# Create a scrollable canvas
    scrollable_frame = Frame(root)
    scrollable_frame.pack(fill=BOTH, expand=True)

    my_canvas = Canvas(scrollable_frame, bg='#F4BFFF')
    my_canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Add a scrollbar to the canvas
    scrollbar = Scrollbar(scrollable_frame, orient=VERTICAL, command=my_canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: update_canvas_width())

    # Create a frame inside the canvas
    inner_frame = Frame(my_canvas, bg='#F4BFFF')
    window = my_canvas.create_window((0, 0), window=inner_frame, anchor="n")

    # Update the position of the inner frame to be centered horizontally
    def update_canvas_width(event=None):
        my_canvas.update_idletasks()
        canvas_width = my_canvas.winfo_width()
        frame_width = inner_frame.winfo_width()
        my_canvas.itemconfig(window, width=frame_width, anchor="n")
        my_canvas.coords(window, (canvas_width - frame_width) / 1.58, 0)
        my_canvas.configure(scrollregion=my_canvas.bbox("all"))

    my_canvas.bind('<Configure>', update_canvas_width)
    z=0
    # Display the fixtures
    for i in range(0, size-1, 2):
        fixtures = f'FIXTURE {z+1}\n{teams[i]} v/s {teams[i+1]}\n'
        Label(inner_frame, text=fixtures, font=('Times New Roman', 14, 'bold'), fg='purple', bg='#F4BFFF',bd=3,relief=RIDGE).pack(fill=X,pady=10)
        z+=1

    # Enable mouse wheel scrolling
    def _on_mouse_wheel(event):
        my_canvas.yview_scroll(-1 * int(event.delta / 120), "units")

    my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

btn = Frame(root, width=1370, bd=4, bg='#F4BFFF')
btn.pack(side=TOP, fill=X)
sbt_btn = Button(btn, text='Predict Fixtures', bg='#DFC5FE', width=15, bd=4, command=predictions)
sbt_btn.pack(side=TOP)

root.mainloop()
