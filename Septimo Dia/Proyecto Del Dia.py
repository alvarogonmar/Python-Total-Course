class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,  nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: ${self.balance}'
    
    def depositar(self, monto_depositado):
        self.balance += monto_depositado
        print('Deposito aceptado')
        
    def retiro(self, monto_retirado):
        if self.balance >= monto_retirado:
            self.balance -= monto_retirado
            print('Retiro realizado')
        else:
            print('Fondos insuficientes')

def crear_cliente():
    nombre_cl = input('Ingrese su nombre:   ')
    apellido = input('ingrese su apellido:   ')
    numero_cuenta = input('Ingrese numero de cuenta:   ')
    cliente1 = Cliente(nombre_cl, apellido, numero_cuenta)
    return cliente1

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 'S':
        print('Elije: D = Depositar, R Retirar, S Salir')
        opcion = input()

        if opcion == 'D':
            monto_dep = int(input('Monto a depositar: '))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_ret = int(input('Monto a retirar'))
            mi_cliente.retiro(monto_ret)
        print(mi_cliente)

    print('Gracias')

inicio()