# import PySimpleGUI as sg
#
# sg.theme('DarkAmber')  # 设置当前主题
# # 界面布局，将会按照列表顺序从上往下依次排列，二级列表中，从左往右依此排列
# layout = [[sg.Text('Some text on Row 1')],
#           [sg.Text('Enter something on Row 2'), sg.InputText()],
#           [sg.Button('Ok'), sg.Button('Cancel')]]
#
# # 创造窗口
# window = sg.Window('Window Title', layout)
# # 事件循环并获取输入值
# while True:
#     event, values = window.read()
#     if event in (None, 'Cancel'):  # 如果用户关闭窗口或点击`Cancel`
#         break
#     print('You entered ', values[0])
#
# window.close()

