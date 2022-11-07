from car import Car
from account import Account
from UberX import UberX

if __name__ == "__main__":
  print("Hola Mundo")

  car = Car("AMS234", Account("Andres Herrera", "ANDA876"))
  print(vars(car))
  print(vars(car.driver))

  # car2 = Car()
  # car2.license = "QWE567"
  # car2.driver = "Martha"
  # print(vars(car2))

  uberX = UberX("QWE567", Account("Anais Salazar", "AND987"), "Chevrolet", "Spark")
  print(vars(uberX))
  print(vars(uberX.driver))