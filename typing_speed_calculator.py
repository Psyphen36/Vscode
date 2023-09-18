import curses
import random
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr('Welcome to the Speed Typing Test!')
    stdscr.addstr('\nPress anything to begin!')
    stdscr.refresh()
    stdscr.getch()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f'WPM: {wpm}')

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)

        if char.isprintable():
            stdscr.addstr(0, i, char, color)

def load_text():
    with open('Config.txt', 'r') as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def wpm_test(stdscr):
    target_text = load_text()
    current_text = ""
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time,1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr,target_text,current_text,wpm)
        stdscr.refresh()

        if current_text == target_text:
            stdscr.nodelay(False)
            break

        key = stdscr.getch()
        if key == curses.KEY_BACKSPACE:
            if len(current_text) > 0:
                current_text = current_text[:-1]

        if len(current_text) < len(target_text) and ord(chr(key)) >= 34 and ord(chr(key)) <= 127:
            current_text += chr(key)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, 'You completed the text! Press any key to continue...')
        key = stdscr.getch()
        if ord(key) == 27:
            break
if __name__ == '__main__':
    curses.wrapper(main)