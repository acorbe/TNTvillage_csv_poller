import pandas as pd
import PySimpleGUI as sg

df = pd.read_csv("./dump_release_tntvillage_2019-08-30.csv")

def table_example():
    sg.set_options(auto_size_buttons=True)
    data = df.iloc[:50].values.tolist()
    #print (data)
    layout = [
        [sg.Input(size=(20, 1), enable_events=True, key='-INPUT-')],        
        [sg.Button('Chrome'), sg.Button('Exit')],
        [sg.Table(values=data,
                  headings=list(df.columns),
                  key='-TABLE-',
                  display_row_numbers=True,
                  auto_size_columns=False,
                  num_rows=min(25, len(data)))]
    ]

    window = sg.Window('Table', layout, grab_anywhere=False)
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):                # always check for closed window
            break
        if values['-INPUT-'] != '':                         # if a keystroke entered in search field
            search = df[df.TITOLO.str.contains(values['-INPUT-'])] #values['-INPUT-']
            window['-TABLE-'].update(search.iloc[:50].values.tolist())
            #new_values = [x for x in names if search in x]  # do the filtering
            #window['-LIST-'].update(new_values)     # display in the listbox
        else:
            # display original unfiltered list
            #window['-LIST-'].update(names)
            # if a list item is chosen
            pass
        if event == '-LIST-' and len(values['-LIST-']):
            sg.popup('Selected ', values['-LIST-'])
    window.close()


table_example()
    
