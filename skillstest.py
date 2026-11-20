from pyscript import document

# Dictionary info about nonmetals
# Element symbol: Element name, Atomic number, Atomic mass

elements = {"H": ('Hydrogen', 1, 1.008), 
           "He" : ('Helium', 2, 4.0026),
           "B" : ('Boron', 5, 10.81),
           "C" : ('Carbon', 6, 12.011),
           "N" : ('Nitrogen', 7, 14.007),
           "O" : ('Oxygen', 8, 15.999),
           "F" : ('Fluorine', 9, 18.998),
           "Ne" : ('Neon', 10, 20.180),
           "Si" : ('Silicon', 14, 28.085),
           "P" : ('Phosphorus', 15, 30.974),
           "S" : ('Sulfur', 16, 32.06),
           "Cl" : ('Chlorine', 17, 35.45),
           "Ar" : ('Argon', 18, 39.948),
           "Ge" : ('Germanium', 32, 72.630),
           "As" : ('Arsenic', 33, 74.922),
           "Se" : ('Selenium', 34, 78.971),
           "Br" : ('Bromine', 35, 79.904),
           "Kr" : ('Krypton', 36, 83.798),
           "Sb" : ('Antimony', 51, 121.76),
           "Te" : ('Tellurium', 52, 127.60),
           "I" : ('Iodine', 53, 126.90),
           "Xe" : ('Xenon', 54, 131.29),
           "Rn" : ('Radon', 86, 222), }
            
           


# function to search your element
def search_element(e):
    #Get the input from HTML

    Element1 = document.getElementById("element1").value
    # retrieve information from the dictionary
    result = elements.get(Element1, ('Element not found', "-", "-"))
    # display the result in html
    document.getElementById("symbol").innerText = Element1
    document.getElementById("name").innerText = result[0]
    document.getElementById("Atomic#").innerText = result[1]
    document.getElementById("AtomicMass").innerText = result[2]
    
