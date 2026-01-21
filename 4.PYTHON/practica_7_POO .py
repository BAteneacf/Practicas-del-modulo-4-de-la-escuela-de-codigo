# Práctica 7, POO, todos los ejercicios juntos

class Persona:

  # Constructor> se ejecuta cada que creamos el objeto y sirve para inicializar sus propiedades
      def __init__(self, nombre="Anonimo", age=0, DNI="N.A."):
        # =====================================================================
        self.nombre = nombre
        self.edad = age
        self.DNI = DNI

      def mostrar (self):
        print(f"Hola yo soy {self.nombre}, tengo {self.edad} años y mi DNI es {self.DNI}")

      def esMayorDeEdad(self):
        esMayor=False
        if self.edad >= 18:
          esMayor=True
        return esMayor

      def setEdad(self, anios):
          if anios >= 0 and anios <= 125:
            self.edad=anios
          else:
            self.edad=0
            print("Estas distraído")
      def getEdad(self):
        return self.edad

      def getNombre(self):
        return self.nombre


class Cuenta:

  def __init__(self,titular=None, cantidad=0):
    self.setTitular(titular)
    self.setCantidad(cantidad)

  def setCantidad(self, cantidad):
    if cantidad <0:
      print ("Pusiste negativos")
      self.cantidad=0
    else:
      self.cantidad=cantidad

  def setTitular(self, titular):
    self.titular=titular

  def ingresar (self, cantidad):
    self.setCantidad(cantidad)

  def getTitular(self):
    return self.titular

  def getCantidad(self):
    return self.cantidad

  def retirar(self,monto):
    if monto>0 and monto<=self.cantidad:
      self.cantidad=self.cantidad-monto
    else:
      print("no puedes retirar")

  def _str_(self):
    pollito = f"titular: {self.titular.getNombre()} cantidad: {self.getCantidad()}"
    return pollito

  def mostrar(self):
      print(self._str_())

class CuentaJoven(Cuenta):

  def __init__(self,titular=None, cantidad=0, bonificacion=0):
    if self.esTitularValido(titular):
      Cuenta.__init__(self, titular, cantidad) #Constructor de padre
      self.setBonificacion(bonificacion) #dif
    else:
      personaGenerica = Persona()
      Cuenta.__init__(self, personaGenerica, cantidad) #Constructor de padre/madre/ancestro/superclase
      self.setBonificacion(bonificacion) #dif
      #print("el titular no tiene edad para este tipo de cuentas, se va a crear l acuenta con titular generico")

  def setBonificacion(self, cantidad):
    if cantidad <0:
      print ("Pusiste negativos")
      self.cantidad=0
    else:
      self.bonificacion=cantidad

  def esTitularValido(self, persona):
    es=False
    annos=persona.getEdad()
    if annos>=18 and annos <25:
      es=True
    return es

  def getBonificacion(self):
    return self.bonificacion

  def retirar(self,monto):
    if self.esTitularValido(self.titular):
      if monto>0 and monto<=self.cantidad:
        self.cantidad=self.cantidad-monto
      else:
        print("no puedes retirar")

  def __str__(self):
    pollito = Cuenta._str_(self)
    pollito = "cuenta joven " + pollito
    pollito = pollito + f" bonificacion: {self.getBonificacion()}"
    return pollito

  def mostrar(self):
      print(self._str_())

print("inicial las pruebas:")
x = Persona()
karina =  Persona("Karina García", 32, "PACK330022")
mrx = Persona("Señorito X", 21, "PACK330089")
cuentax = Cuenta(karina, 100)
cuentay = CuentaJoven(karina, 100, 50)
karina.mostrar()
cuentax.mostrar()
cuentay.mostrar()
cuentax.retirar(90)
cuentax.mostrar()
# viendo si funciona el método  esTitularValido(karina)
cuentay.esTitularValido(karina)
print("fin de las pruebas")