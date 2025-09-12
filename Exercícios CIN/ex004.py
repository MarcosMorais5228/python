arthur = int(input())
luiz = int(input())
pedro = int(input())
horas = int(input())

total_arthur = arthur*horas
total_luiz = luiz*horas
total_pedro = pedro*horas

arthur_luiz = int((total_arthur + total_luiz + abs(total_arthur - total_luiz))/2)
arthur_luiz_pedro = int((arthur_luiz + total_pedro + abs(arthur_luiz - total_pedro))/2)

print(arthur_luiz_pedro)