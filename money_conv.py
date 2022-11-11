import PySimpleGUI as sg
from PIL import Image
import time
import io

BGN_EUR = 0.51129188
EUR_BGN = 1.95583

# bgn = float(input('BGN '))
# print('EUR', round(bgn*BGN_EUR, 6))
img = Image.open('symbol-europe-currency-illustration-sm.jpeg')
# img.thumbnail((300, 300))
bio = io.BytesIO()
img.save(bio, format='PNG')

if 7 < time.localtime(time.time()).tm_hour < 18:
    sg.theme('Reddit')
else:
    sg.theme('Topanga')
layout = [
    [sg.Combo(('BGN', 'EUR'), default_value='BGN', key='-IN-CURRENCY-'),
     sg.InputText(size=20, key='-IN-'), sg.Button('Convert')],
    [sg.Text('EUR', size=5, key='-OUT-CURRENCY-'),
     sg.InputText(size=20, readonly=True, key='-OUT-')],
    [sg.Image(data=bio.getvalue(), key='-OUT-IMAGE-')]
]

window = sg.Window('Money Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'Convert' and values['-IN-'] != '':
        if values['-IN-CURRENCY-'] == 'BGN':
            window['-OUT-'].update(round(float(values['-IN-'])*BGN_EUR, 6))
            window['-OUT-CURRENCY-'].update('EUR')
            window['-OUT-IMAGE-'].update(
                'lovepik-villain-carrying-euro-symbol-png-image_401759462_wh300.png')
        else:
            window['-OUT-'].update(round(float(values['-IN-'])*EUR_BGN, 6))
            window['-OUT-CURRENCY-'].update('BGN')
            window['-OUT-IMAGE-'].update('Belgium.png')

window.close()
