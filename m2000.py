#!/usr/bin/env python3

"""
M2000 by Toka
"""

import PySimpleGUI as sg
import random
import string
import time


def main():
    while True:
        window_ui()


def window_ui():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Word to guess:', size=(15, 1)), sg.InputText('', size=(30, 1), key='_word_'),
         ],
        [sg.Text('Operations:', size=(15, 1)), sg.InputText('', size=(30, 1), key='_ops_')
         ],
        [sg.Text('Output:', size=(15, 1)), sg.Multiline('', size=(30, 5), key='_output_'),
         ],
        [sg.Button('Start'), sg.Button('Exit')],
    ]
    window = sg.Window('M2000', layout)
    while True:  # The Event Loop
        event, values = window.read()
        if event in (None, 'Exit'):
            exit(0)
        elif event in 'Start':
            word_guess = values['_word_']
            operations = values['_ops_']
            correct = 0
            start_time = time.time()
            start_op = operations
            if operations.isdigit():
                while int(operations) != -1:
                    ai_word = ""
                    for i in word_guess:
                        random_letter = random.choice(string.ascii_letters)
                        ai_word = ai_word + random_letter
                    x = int(operations)
                    operations = x - 1
                    if operations >= 0:
                        if ai_word.upper() == word_guess.upper():
                            x = correct
                            correct = x + 1
                    else:
                        elapsed_time = time.time() - start_time
                        elapsed_time_mis = elapsed_time * 1000000
                        elapsed_time_ms = elapsed_time_mis / 1000
                        elapsed_time_s = elapsed_time_ms / 1000
                        if elapsed_time == 0.0:
                            difference_s = start_op
                        elif elapsed_time != 0.0:
                            difference_mis = int(start_op) / int(elapsed_time_mis)
                            difference_ms = difference_mis * 1000
                            difference_s = difference_ms * 1000
                        output = "Guesses in total: {0}\nGuesses pr. second: {1}\nSeconds to complete: {2}s\nCorrect " \
                                 "guesses: {3}\nWord to guess: {4}".format(format(int(start_op), ','),
                                                                           format(round(int(difference_s)), ','),
                                                                           round(elapsed_time_s, 5), format(correct, ','),
                                                                           word_guess)
                        window.FindElement('_output_').Update(output)

    window.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
