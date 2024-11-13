salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

financial_cushion = 0
count_months = 0

while count_months < months:
    financial_cushion += spend - salary
    spend += spend * increase
    count_months += 1

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(financial_cushion))
