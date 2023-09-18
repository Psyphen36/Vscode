import tkinter as tk
import random
import time

class TypingCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title('Typing Calculator')
        self.root.geometry('800x600')
        self.root.resizable(False, False)

        self.target_text = self.load_text()
        self.current_text = ''
        self.start_time = None
        self.elapsed_time = None

        self.title_label = tk.Label(self.root, text='Typing Calculator', font=('Arial', 24))
        self.title_label.pack(pady=20)

        self.text_frame = tk.Frame(self.root)
        self.text_frame.pack(pady=20)

        self.target_label = tk.Label(self.text_frame, text=self.target_text, font=('Arial', 18))
        self.target_label.pack(side=tk.LEFT)

        self.current_label = tk.Label(self.text_frame, text='', font=('Arial', 18))
        self.current_label.pack(side=tk.LEFT)

        self.wpm_label = tk.Label(self.root, text='WPM: 0', font=('Arial', 18))
        self.wpm_label.pack(pady=20)

        self.start_button = tk.Button(self.root, text='Start', font=('Arial', 18), command=self.start_test)
        self.start_button.pack(pady=20)

    def load_text(self):
        with open('Config.txt', 'r') as f:
            lines = f.readlines()
            return random.choice(lines).strip()

    def start_test(self):
        self.start_button.config(state=tk.DISABLED)
        self.root.bind('<Key>', self.on_key_press)
        self.root.focus_set()
        self.current_text = ''
        self.start_time = time.time()
        self.update_text()

    def on_key_press(self, event):
        if self.start_time is None:
            return

        key = event.char
        if key == '\r':
            self.complete_test()
        elif key == '\x08':
            if len(self.current_text) > 0:
                self.current_text = self.current_text[:-1]
        elif len(self.current_text) < len(self.target_text) and key.isprintable():
            self.current_text += key

        self.update_text()

    def complete_test(self):
        self.elapsed_time = time.time() - self.start_time
        wpm = round(len(self.current_text) / (self.elapsed_time / 60) / 5)
        self.wpm_label.config(text=f'WPM: {wpm:.0f}')
        self.root.unbind('<Key>')
        self.start_button.config(text='Restart', state=tk.NORMAL)

    def update_text(self):
        self.current_label.config(text=self.current_text)
        target_text_list = list(self.target_text)
        current_text_list = list(self.current_text)
        for i in range(len(target_text_list)):
            if i < len(current_text_list):
                if current_text_list[i] == target_text_list[i]:
                    target_text_list[i] = '<span style="color:green">{}</span>'.format(target_text_list[i])
                else:
                    target_text_list[i] = '<span style="color:red">{}</span>'.format(target_text_list[i])
            else:
                target_text_list[i] = '<span>{}</span>'.format(target_text_list[i])

        self.target_label.config(text=''.join(target_text_list))

if __name__ == '__main__':
    root = tk.Tk()
    app = TypingCalculator(root)
    root.mainloop()
