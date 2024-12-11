money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

current_balance = money_capital + salary  # Деньги в первый месяц
count_months = 0

while current_balance >= spend:
    current_balance -= spend
    current_balance += salary
    spend += spend * increase
    count_months += 1

print("Количество месяцев, которое можно протянуть без долгов:", count_months)
