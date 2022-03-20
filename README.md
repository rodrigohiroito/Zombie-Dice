# Zombie-Dice :zombie:

Implementação digital do jogo Zombie Dice

Projeto da disciplina de Raciocínio Computacional do Curso de Tecnologia em Análise e Desenvolvimento de Sistemas da Pontifícia Universidade Católica do Paraná - PUCPR

## O jogo 🎮

Coma cérebros. Não leve tiros.

Em **Zombie Dice**, você é um zumbi. Você quer cééérebros - mais cérebros do que qualquer um dos seus amigos zumbis. Os 13 dados personalizados são suas vítimas. Abuse da sorte para comer seus cérebros, mas pare de rolar os dados antes que os tiros de espingarda encerrem seu turno. Cada jogo leva de 10 a 20 minutos e pode ser ensinado em uma única rodada.

A cada turno, você retira e rola três dados do tubo. Um símbolo de cérebro 🧠 vale um ponto ao final da rodada, enquanto pegadas 👣 permitem que você role novamente esse dado. Por outro lado, tiros de espingarda 💥 são ruins, pois se você receber três tiros durante seu turno, ele acaba e você não recebe ponto algum. Após rolar três dados, você decide se quer pontuar seu atual acervo de cérebros ou se quer abusar da sorte pegando novos dados até que tenha três novamente e rolando-os mais uma vez.

### Regras 📓

No seu turno, pegue e role 3 dados do tubo.

Cada um deles representa uma pobre vítima a ser atacada. Os dados <font color="red">vermelhos</font> são os mais difíceis. Os <font color="green">verdes</font> são os mais fáceis e os <font color="yellow">amarelos</font> são médios.

Os dados possuem 3 símbolos:

- 🧠 Cérebro - Você devorou o cérebro de sua vítima.
- 💥 Espingarda - Sua vítima revidou!
- 👣 Pegadas - Sua vítima escapou.

Se tiver rolado 3 dados com a face da Espingarda, em qualquer momento, seu turno acabou. Caso contrário, você pode optar por **parar e marcar pontos** ou **continuar**.

Se voce decidir **parar**, cada Cérebro que você rolou será computado como 1 ponto, e todos os dados voltarão ao tubo. O próximo jogador inicia seu turno.

Se você escolher **continuar**, os dados não retornarão ao tubo. Sempre que você rolar dados, você vai rolar três por vez. Primeiro, você deverá pegar todas as Pegadas que estejam à sua frente, depois, pegue dados suficientes do tubo (se for preciso) até completar três e role-os novamente.

Depois de pegar novos dados, você não pode decidir **parar**... você tem que rolar.

Separe os Cérebros e as Espingardas. Se você rolar a terceira Espingarda seu turno acaba e você **não marca pontos**. Caso contrário, você pode parar e marcar pontos, ou rolar os dados novamente...

Se você não tiver 3 dados sobrando no tubo, os dados de Cérebro já rolados serão adicionados de volta ao tubo. É só continuar...

Jogue até alguém chegar a 13 Cérebros. Termina a rodada (todos devem jogar o mesmo número de turnos). Quem tiver devorado mais Cérebros até o final dessa rodada é o vencedor. Se houver um empate, os líderes (apenas) jogam uma rodada de desempate.

## Versões 💻

- 0.1: protótipo inicial apresentado como Atividade Somativa 1. Protótipo deve apresentar:
  - Manipulação de variáveis e constante;
  - Uso de estruturas condicionais (if, elif e else) na implementação em Python;
  - Uso de operadores lógicos e relacionais;
  - Uso de estruturas de repetição (for e while)
