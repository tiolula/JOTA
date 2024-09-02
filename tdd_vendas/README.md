# Dojo de Vendas! 🤑

Neste Dojo vamos treinar testes automatizados para um sistema que ainda não existe. Vamos criá-lo do zero, começando pelos testes, e os testes vão fazer emergir o código de negócio.

## Nosso fluxo de desenvolvimento

Passo a passo do nosso fluxo:

1. Escrever um teste e rodar
2. Escrever a solução mínima e rodar os testes
3. Melhorar o código e rodar os testes
4. Voltar ao passo 1

## Regras de Negócio

Nossa empresa, a YPISSILON, decidiu alavancar as vendas do seu produto YPISSILON PRO através de pessoas de vendas focados em B2B. essas pessoas têm a missão de acionar sua rede de contatos em grandes corporações e vender nosso produto através de pacotes que podem incluir quantas pessoas da empresa forem necessárias.

As pessoas que vendem recebem comissão pelas vendas realizadas. A comissão é calculada em cima do valor de venda do pacote, conforme a tabela a seguir:

| Valor mensal do pacote vendido | Percentual de comissão |
|--------------------------------|------------------------|
| Até R$10.000,00                | 5%                     |
| Até R$20.000,00                | 7%                     |
| Acima de R$20.000,00           | 10%                    |

> ⚠️ Importante: O YPISSILON nunca deve tomar prejuízo!


## Nosso desafio

Não nos preocuparemos com interface de usuário nesse momento. O desafio aqui é construir a calculadora que dirá, a partir do valor vendido, qual é o valor da comissão que deve ser paga à pessoa que fez a venda.