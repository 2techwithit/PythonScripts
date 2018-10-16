import PySimpleGUI as sg

layout = [ [sg.Txt('Enter values to calculate')],
           [sg.In(size=(8,1), key='numerator')],
           [sg.Txt('_'  * 10)],
           [sg.In(size=(8,1), key='denominator')],
           [sg.Txt('', size=(8,1), key='output')  ],
           [sg.ReadButton('Calculate', bind_return_key=True)]]

window = sg.Window('Math').Layout(layout)

while True:
    button, values = window.Read()

    if button is not None:
        try:
            numerator = float(values['numerator'])
            denominator = float(values['denominator'])
            calc = numerator / denominator
        except:
            calc = 'Invalid'

        window.FindElement('output').Update(calc)
    else:
        break