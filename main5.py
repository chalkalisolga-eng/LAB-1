# введіть десяткове число
decimal_number = int(input())

# Використовую вбудовану функцію hex()
hex_number = hex(decimal_number)

# Виводю результат, видаляючи префікс '0x'
print(hex_number[2:])
