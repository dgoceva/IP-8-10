import PySimpleGUI as sg
import time

BGN_EUR = 0.51129188

# bgn = float(input('BGN '))
# print('EUR', round(bgn*BGN_EUR, 6))

if 7 < time.localtime(time.time()).tm_hour < 18:
    sg.theme('Reddit')
else:
    sg.theme('Topanga')
layout = [
    [sg.Text('BGN'), sg.InputText(size=20, key='-IN-'), sg.Button('Convert')],
    [sg.Text('EUR'), sg.InputText(size=20, readonly=True, key='-OUT-')]
]

window = sg.Window('BGN to EUR Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'Convert' and values['-IN-'] != '':
        window['-OUT-'].update(round(float(values['-IN-'])*BGN_EUR, 6))

window.close()
