from ui import get_ui, get_broarcaster
from img import get_img

import threading 

def f1():
    ui = get_ui("extinctCoder")
    b = get_broarcaster()
    b.loop_start
    ui.mainloop()

    return

def f2():
    # get_img("extinctCoder")
    return


t1 = threading.Thread(target=f1) 
# t2 = threading.Thread(target=f2) 

t1.start()
# t2.start()

t1.join() 
# t2.join() 
