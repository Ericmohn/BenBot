import random
import PySimpleGUI as sg

class YesNoBot:
    def __init__(self):
        self.answers = [
            'Yes!',
            'No!',
            'Maybe!'
        ]

    def Start(self):
        # Layout
        layout = [
            [sg.Text('Ask your question:')],
            [sg.Input()],
            [sg.Output(size=(20,10))],
            [sg.Button('Answer!')]
        ]
        # Window
        self.window = sg.Window('Ben Bot', layout=layout)
        while True:
            # Read the values
            self.events, self.values = self.window.Read()
            # Run the values
            if self.events == 'Answer!' :
                print(random.choice(self.answers))

benbot = YesNoBot()
benbot.Start()