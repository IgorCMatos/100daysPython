
bill = float(input("Quanto foi sua conta? "))
tip = float(input("O quanto de gorgeta? 10, 12, 15? "))
people = int(input("Quantas pessoas vao dividir a conta? "))

tip_percentage = tip / 100
bill_total = bill + (bill * tip_percentage)

bill_per_people = bill_total / people

print(f"O valor total com a gorjeta ficou R${bill_total:.2f}")
print(f"e o valor da conta ficou R${bill_per_people:.2f} por pessoa")