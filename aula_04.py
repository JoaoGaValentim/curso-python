"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
A palavra global faz ela ser usada no escopo interno
de uma função, mesmo sendo o do módulo
"""

operation_command = 1


def system_start():
    # global operation_command  # má prática
    operation_command = 3

    def internal_model():
        internal_model_command = 2
        print(operation_command, internal_model_command)

    internal_model()


print(operation_command)  # global variable of this model
system_start()
print(operation_command)  # global variable of this model
