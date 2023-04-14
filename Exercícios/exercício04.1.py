salario1 = float(input("Digite seu primeiro salário "))
salario2 = float(input("Digite seu segundo salário "))
salario3 = float(input("Digite seu terceiro salário "))
salario4 = float(input("Digite seu quarto salário "))

soma = salario1 + salario2 + salario3 + salario4

polimorfismo = '*'*20
print(polimorfismo, 'CALCULADORA', polimorfismo)

print('''o primeiro salario digitado foi {:.2f}
\n o segundo salario digitado foi {:.2f}
\n o terceiro salario digitado foi {:.2f}
\n o quarto salario digitado foi {:.2f}
\n a soma dos salarios foi: {:.2f}'''.format(salario1, salario2, salario3, salario4, soma))