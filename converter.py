import PySimpleGUI as sg
from Conversor import Conversor

sg.theme("Dark Green 2")

sg.set_options(element_padding=(0, 0))


layout = [
          [sg.Text("Choose Unit to Convert", size=(44,1), justification= "center")],
          [sg.Text()],
          [
            sg.Combo(values=("Celsius", "Farenheit", "Kelvin","Meters", "Miles", "Feet","Kilometers","Nautic Miles"),
            default_value = "From",
            readonly = True,
            size=(19,2),
            key="-COMBO1-"),
            sg.Text(size=(4,1)),
            sg.Combo(values=("Celsius", "Farenheit", "Kelvin","Meters", "Miles", "Feet","Kilometers","Nautic Miles"),
            default_value= "To",
            readonly = True,
            size=(19,2),
            key="-COMBO2-")
          ],
          [sg.Text("Insert Number", key="-TXT2-")],
          [
            sg.Input(key="-In-", size=(19,2), enable_events = True),
            sg.Text(size=(1,1)),
            sg.Button("=>", size=(1,1)),
            sg.Text(size=(1,1)),
            sg.Input(key="-Out-", size=(19,2),
             enable_events = True,
             readonly=True)
          ],
          [sg.Text()],
          [sg.Button("Reset"),
           sg.Text(),
           sg.Button("Close")]]

window = sg.Window("UNIT CONVERSOR",
         layout,
         font= 8,
         icon=sg.EMOJI_BASE64_HAPPY_JOY, keep_on_top=True)

def equal_button():
    val_1 = window["-In-"].get()
    pd_1 = window["-COMBO1-"].get()
    pd_2 = window["-COMBO2-"].get()

    if pd_1 == pd_2:
        window["-Out-"].update(val_1)

    elif pd_1 == "Celsius" and pd_2 == "Farenheit":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.celsius_to_farenheit())

    elif pd_1 == "Celsius" and pd_2 == "Kelvin":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.celsius_to_kelvin())

    elif pd_1 == "Farenheit" and pd_2 == "Celsius":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.farenheit_to_celsius())

    elif pd_1 == "Farenheit" and pd_2 == "Kelvin":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.farenheit_to_kelvin())

    elif pd_1 == "Kelvin" and pd_2 == "Celsius":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.kelvin_to_celsius())

    elif pd_1 == "Kelvin" and pd_2 == "Farenheit":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.kelvin_to_farenheit())

    elif pd_1 == "Kilometers" and pd_2 == "Miles":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.kilometers_to_miles())

    elif pd_1 == "Miles" and pd_2 == "Kilometers":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.miles_to_kilometers())

    elif pd_1 == "Miles" and pd_2 == "Meters":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.miles_to_kilometers()*1000)

    elif pd_1 == "Meters" and pd_2 == "Miles":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.kilometers_to_miles()/1000)

    elif pd_1 == "Nautic Miles" and pd_2 == "Kilometers":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.nautic_miles_to_kilometers())

    elif pd_1 == "Nautic Miles" and pd_2 == "Meters":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.nautic_miles_to_kilometers()*1000)

    elif pd_1 == "Meters" and pd_2 == "Nautic Miles":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.kilometers_to_nautic_miles()/1000)

    elif pd_1 == "Kilometers" and pd_2 == "Nautic Miles":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.kilometers_to_nautic_miles())

    elif pd_1 == "Kilometers" and pd_2 == "Nautic Miles":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.kilometers_to_nautic_miles())

    elif pd_1 == "Miles" and pd_2 == "Nautic Miles":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.miles_to_nautic_miles())

    elif pd_1 == "Nautic Miles" and pd_2 == "Miles":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.nautic_miles_to_miles())

    elif pd_1 == "Meters" and pd_2 == "Feet":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.meters_to_feet())

    elif pd_1 == "Feet" and pd_2 == "Meters":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.meters_to_feet())

    elif pd_1 == "Feet" and pd_2 == "Kilometers":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.meters_to_feet()/1000)

    elif pd_1 == "Kilometers" and pd_2 == "Feet":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.meters_to_feet()*1000)

    elif pd_1 == "Feet" and pd_2 == "Kilometers":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.meters_to_feet()/3281)

    elif pd_1 == "Meters" and pd_2 == "Kilometers":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.meters_to_kilometers())

    elif pd_1 == "Kilometers" and pd_2 == "Meters":
        convert = Conversor()
        convert.set_extern_value(val_1)
        window["-Out-"].update(convert.kilometers_to_meters())

    else:
        window["-Out-"].update("ERROR")



while True:
    event, values = window.read()

    val_1 = window["-In-"].get()

    try:
        x = float(val_1)
    except ValueError:
        window["-In-"].update("Must be a Number")


    if event == "Close" or event == sg.WIN_CLOSED:
        break

    if event == "=>":
        equal_button()

    if event == "Reset":
        window["-In-"].update("")
        window["-Out-"].update("")
        window["-COMBO1-"].update("From")
        window["-COMBO2-"].update("To")

window.close()
