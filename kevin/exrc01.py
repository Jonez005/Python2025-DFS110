
class Conta:
    def __init__(self, titular: str, numero: str, saldo: float = 0):
        self.titular = titular
        self.numero = numero

        if saldo < 0:
            raise ValueError('O saldo inicial deve ser maior ou igual a 0')

        self.saldo = saldo

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de depósito deve ser maior que 0')
        
        self.saldo += valor

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de saque deve ser maior que 0')
        
        if valor > self.saldo:
            raise ValueError('Saldo insuficiente.')
        
        self.saldo -= valor

    def transferir(self, valor: float, conta_destino: 'Conta'):
        self.sacar(valor)
        conta_destino.depositar(valor)

    def __str__(self):
        return f'{self.titular} (Nº{self.numero}) - R${self.saldo:.2f}'


c1 = Conta('Davi', '00001', 100)
c2 = Conta('Renato', '00002', 10000)

# Depositar
print(c1)

try:
    valor = float(input('Quanto deseja depositar? '))
    c1.depositar(valor)
    print(f'Valor de R${valor:.2f} depósitado com sucesso.')
except ValueError as err:
    print(err)

# Sacar
print(c1)

try:
    valor = float(input('Quanto deseja sacar? '))
    c1.sacar(valor)
    print(f'Valor de R${valor:.2f} sacado com sucesso.')
except ValueError as err:
    print(err)

# Transferir
print(c1)
print(c2)

try:
    valor = float(input('Quanto deseja transferir? '))
    c1.transferir(valor, c2)
    print(f'Valor de R${valor:.2f} transferido com sucesso para a conta Nº{c2.numero}.')
except ValueError as err:
    print(err)

print(c1)
print(c2)