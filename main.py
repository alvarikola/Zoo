from coleccionAnimal import ColeccionAnimal
from animal import Animal
from coleccionTrabajador import ColeccionTrabajador
from trabajador import Trabajador
from coleccionHabitat import ColeccionHabitat
from habitat import Habitat

cc = ColeccionAnimal().leer()

# print(cc.buscar(Animal('Gato')))
# print(cc.insertar(Animal('Gato')))
# cc.borrar(Animal('Perro'))
# cc.actualizar("Quedan 2 semanas de clase", "Hola qué tal!")
cc = [("uno","dos")] + cc
print(cc)