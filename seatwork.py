from pyscript import document,display

Grade_7 = {'Renn Santos', 'Manu Correa', 'Jacob Minguillo'}
Grade_8 = {'Robert Prevost', 'Francis Assisi', 'Thomas Prevost'}
Grade_9 = {'Edrian Correa', 'Andre Pagud', 'Ramone Betilez'}
Grade_10 = {'Dylan Alip', 'Sean Ho', 'Dylan Harper'}

def Add(event=None):

    Grade_7 = {'Renn Santos', 'Manu Correa', 'Jacob Minguillo'}
    Grade_8 = {'Robert Prevost', 'Francis Assisi', 'Thomas Prevost'}
    Grade_9 = {'Edrian Correa', 'Andre Pagud', 'Ramone Betilez'}
    Grade_10 = {'Dylan Alip', 'Sean Ho', 'Dylan Harper'}

    combine = Grade_7 | Grade_8 | Grade_9 | Grade_10

    first_name = document.getElementById("First").value
    last_name = document.getElementById("Last").value
    combined_name = f"{first_name} {last_name}"

    display(combine.add(combined_name) , target="output1")