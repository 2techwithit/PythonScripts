import random
import PySimpleGUI as sg


# def getdice():
#     xdice = int(input('How many dice would you like to roll? '))
#     ysides = int(input('How many sides do the dice have? '))
#     zero = 0
#     while True:
#         if xdice > zero and ysides > zero:
#             break
#         elif xdice <= zero <= ysides:
#             print('Please enter a non-zero integer for the number of dice.')
#             xdice = int(input())
#         elif xdice >= zero >= ysides:
#             print('Please enter a non-zero integer for the number of sides.')
#             ysides = int(input())
#     roll(xdice, ysides)


def roll(xdice, ysides):
    toroll = xdice
    # print(toroll)
    roll_list = []
    # print('The dice are rolling, may luck be in your favor!')
    for x in range(toroll):
        roll = random.randint(1, ysides)
        # print(roll)
        roll_list.append(roll)
    return roll_list


def showrolls(rolls):
    temp_str = ''
    roll_str = ''
    for x in rolls:
        i = str(x)
        if roll_str is temp_str:
            roll_str = temp_str.join(i)
        else:
            roll_str = roll_str + i
        roll_str = roll_str + ','
    return roll_str


if __name__=='__main__':

    layout = [[sg.Txt('Dice Roller', font=('Helvetica', 14))],
              [sg.Txt('Number of Dice', font=('Helvetica', 14)), sg.In(size=(8, 1), key='xdice')],
              [sg.Txt('_' * 16)],
              [sg.Txt('Number of Sides', font=('Helvetica', 14)), sg.In(size=(8, 1), key='ysides')],
              [sg.Txt('', font=('Helvetica', 14), size=(32, 1), key='output')],
              [sg.ReadButton('Roll', bind_return_key=True)]]

    window = sg.Window('Roll Dice').Layout(layout)

    while True:
        button, values = window.Read()
        results = '***'
        if button is not None:
            try:
                xdice = int(values['xdice'])
                ysides = int(values['ysides'])
                throw_dice = roll(xdice, ysides)
                results = showrolls(throw_dice)
            except:
                results = 'Invalid'

            window.FindElement('output').Update(results)
        else:
            break

