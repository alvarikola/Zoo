from textual.app import App, ComposeResult
from textual.events import Mount
from textual.screen import Screen
from textual.widgets import Button, DataTable, Input, Header, Footer
from textual.containers import Horizontal


from coleccionAnimal import ColeccionAnimal
from animal import Animal
from coleccionTrabajador import ColeccionTrabajador
from trabajador import Trabajador
from coleccionHabitat import ColeccionHabitat
from habitat import Habitat

'''
ANIMALES = [
    ("ID", "Nombre"),
]

ANIMALES = [
    ("ID", "Nombre"),
    [(9, 'Perro'),(10, 'Gato')]
]


TRABAJADORES = [
    ("ID", "Nombre"),
    (1, "Juan"),
    (2, "Alvaro"),
    (3, "David"),
]

HABITATS = [
    ("ID", "Nombre"),
    (1, "Playa"),
    (2, "Bosque"),
    (3, "Montaña"),
]
'''


class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header("El zoo de Álvaro")
        yield Horizontal( 
            Button("Animal", id="animal"),
            Button("Trabajador", id="trabajador"),
            Button("Hábitat", id="habitat"),
            Button.error("Salir", id="salir"),
        )
        yield Footer()
        

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "animal":
            self.app.push_screen(AnimalScreen())
        elif event.button.id == "trabajador":
            self.app.push_screen(TrabajadorScreen())
        elif event.button.id == "habitat":
            self.app.push_screen(HabitatScreen())
        elif event.button.id == "salir":
            self.app.exit(str(event.button))

    def on_mount(self) -> None:
        self.title = "El zoo de Álvaro"
        

class AnimalScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header("Animales del zoo") 
        yield DataTable()
        yield Button("Insertar", id="insertar")
        yield Button("Volver", id="volver")
        yield Footer()


    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "volver":
            self.app.push_screen(MainScreen())
        elif event.button.id == "insertar":
            self.app.mytable = "animal"
            self.app.pop_screen()
            self.app.push_screen(InsertarScreen())
            

    def _on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = "row"
        table.zebra_stripes = True
        animales = [("ID", "Nombre")]
        animales += ColeccionAnimal().leer()
        table.add_columns(*animales[0])
        table.add_rows(animales[1:])
        self.title = "Animales del zoo"


class TrabajadorScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header("Trabajadores del zoo") 
        yield DataTable()
        yield Button("Insertar", id="insertar")
        yield Button("Volver", id="volver")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "volver":
            self.app.push_screen(MainScreen())
        elif event.button.id == "insertar":
            self.app.mytable = "trabajador"
            self.app.pop_screen()
            self.app.push_screen(InsertarScreen())

    def _on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = "row"
        table.zebra_stripes = True
        trabajadores = [("ID", "Nombre")]
        trabajadores += ColeccionTrabajador().leer()
        table.add_columns(*trabajadores[0])
        table.add_rows(trabajadores[1:])
        self.title = "Trabajadores del zoo"
        


class HabitatScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header("Habitats del zoo") 
        yield DataTable()
        yield Button("Insertar", id="insertar")
        yield Button("Volver", id="volver")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "volver":
            self.app.push_screen(MainScreen())
        elif event.button.id == "insertar":
            self.app.mytable = "habitat"
            self.app.pop_screen()
            self.app.push_screen(InsertarScreen())

    def _on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = "row"
        table.zebra_stripes = True
        habitats = [("ID", "Descripción")]
        habitats += ColeccionHabitat().leer()
        table.add_columns(*habitats[0])
        table.add_rows(habitats[1:])
        self.title = "Habitats del zoo"


class InsertarScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header("Insertar animales") 
        yield Input(placeholder="Nombre del animal")
        yield Button("Volver", id="volver")
        yield Button("Aceptar", id="aceptar")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "volver":
            # self.app.push_screen("animal")
            self.app.pop_screen()
        elif event.button.id == "aceptar" and self.app.mytable == "animal":
            self.app.ca.insertar(Animal(self.query_one(Input).value))
        elif event.button.id == "aceptar" and self.app.mytable == "trabajador":
            self.app.ct.insertar(Trabajador(self.query_one(Input).value))
        elif event.button.id == "aceptar" and self.app.mytable == "habitat":
            self.app.ch.insertar(Habitat(self.query_one(Input).value))

            
            

    def _on_mount(self) -> None:
        self.title = "Insertar datos"
      
    


class ModesApp(App):
    BINDINGS = [
        ("a", "switch_mode('animal')", "Animal"),  
        ("t", "switch_mode('trabajador')", "Trabajador"),
        ("h", "switch_mode('habitat')", "Habitat"),
        ("q", "switch_mode('main')", "Volver al main"),
        
    ]
    MODES = {
        "main": MainScreen,  
        "animal": AnimalScreen,
        "trabajador": TrabajadorScreen,
        "habitat": HabitatScreen,
        "insertar": InsertarScreen,
    }


    def _on_mount(self) -> None:
        self.ca = ColeccionAnimal()
        self.ct = ColeccionTrabajador()
        self.ch = ColeccionHabitat()
        self.push_screen(MainScreen())     



if __name__ == "__main__":
    app = ModesApp()
    app.run()
