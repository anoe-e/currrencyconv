import requests

print( 'Валюти тільки такого типу: eur, aud, bgn, brl, cad, chf, cny, czk, gbp,\n'\
'hkd, huf, idr, ils, inr, isk, jpy, krw, mxn, myr, nok, nzd,\n'\
'php, pln, ron, sek, sgd, thb, try, usd, zar.')

while True:
    from_currency = str(
        input("Валюта з якої треба перевести: ")).upper()

    to_currency = str(
        input("Валюта на яку треба перевести: ")).upper()

    amount = float(input("Введіть кількість яку потрібно перевести: "))

    response = requests.get(
        f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

    print(
        f"{amount} {from_currency} це {response.json()['rates'][to_currency]} {to_currency}")