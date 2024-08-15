def nota(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    dados = {'quantidade': len(n), 'maior': max(n), 'menor': min(n), 'média': sum(n) / len(n)}
    if sit:
        if dados['média'] >= 7:
            dados['situação'] = 'BOA'
        if dados['média'] <= 5:
            dados['situação'] = 'RUIM'
        else:
            dados['situação'] = 'RAZOÁVEL'
    return dados


x = nota(5.5, 2.5, 1.5, sit=True)
print(x)
# help(nota)
