Treino_de_hoje=(input('Para ver o treino de pernas digite Perna\nPara ver o treino de peito digite Peito\nPara ver o treino de braço digite Braço\nPara ver o treino de costas digite Costas\nPara ver o treino de ombro digite Ombro\nqual treino você deseja consultar?'))




if Treino_de_hoje == 'Perna':
    Pernas_exercicios = ['agachamento', 'leg press 45°', 'extensora', 'abdutora', 'elevação pélvica', 'flexora em pé',
                         'cadeira flexora', 'panturilha']
    print('exercicios de perna da lista:')

    for x in Pernas_exercicios:
        print('-',x)


if Treino_de_hoje == 'Peito':
    Peito_exercicios = ['supino inclinado', 'crucifixo na polia baixa', 'supino reto', 'peck deck', 'supino vertical',
                        'supino reto com halter', 'pullover']
    print('exercicios de Peito da lista:')

    for x in Peito_exercicios:
        print('-',x)


if Treino_de_hoje == 'Braço':
    Braço_exercicios = ['biceps na polia', 'rosca W', 'rosca scot com halter', 'rosca scot', 'rosca martelo',
                        'triceps corda', 'triceps invertido', 'triceps francês']
    print('exercicios de braço da lista:')

    for x in Braço_exercicios:
        print('-',x)

if Treino_de_hoje == 'Costas':
    Costas_exercicio = ['puxada alta', 'postura', 'remada baixa', 'crucifixo inverso', 'remada articulada', 'serrote',
                        'Face pull']
    print('exercicios de costas da lista:')

    for x in Costas_exercicio:
        print('-',x)

if Treino_de_hoje == 'Ombro':
    Ombro_exercicios = ['Face pull', 'elevação lateral', 'elevação frontal na polia', 'desenvolvimento', 'trápezio']
    print('exercicios de ombro da lista:')

    for x in Ombro_exercicios:
        print('-',x)


