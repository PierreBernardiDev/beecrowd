
primeiroInput = str(input('Insira o primeiro dado: ').strip())
segundoInput = str(input('Insira o segundo dado: ').strip())
terceiroInput = str(input('Insira o terceiro dado: ').strip())


animais = [
    ["vertebrado", 
        ["ave", 
            ["carnivoro", ["aguia"]],
            ["onivoro", ["pomba"]]
        ],
        ["mamifero",
            ["onivoro", ["homem"]],
            ["herbivoro", ["vaca"]]
        ]
    ],
    ["invertebrado",
        ["inseto",
            ["hematofago",["pulga"]],
            ["herbivoro",["lagarta"]]
        ],
        ["anelideo",
            ["hematofago",["sanguessuga"]],
            ["onivoro",["minhoca"]]
        ]
    ]
]

if primeiroInput ==  'vertebrado':
    for coluna in animais:
        break
    if segundoInput == 'ave':
        for classe in animais[0][1:]:
            break
        if terceiroInput == 'carnivoro':
            for alimentacao in animais[0][1:]:
                print(alimentacao[0:][1][1][0])
                break
        elif terceiroInput == 'onivoro':
            for alimentacao in animais[0][1:]:
                print(alimentacao[1:][1][1][0])
                break
    elif segundoInput == 'mamifero':
        for classe in animais[0][1:][1:]:
            break
        if terceiroInput == 'onivoro':
            for alimentacao in animais[0][1:][1:]:
                print(alimentacao[0:][1][1][0])
                break
        elif terceiroInput == 'herbivoro':
            for alimentacao in animais[0][1:][1:]:
                print(alimentacao[1:][1][1][0])
                break
elif primeiroInput == 'invertebrado':
    for coluna in animais:
        break
    if segundoInput == 'inseto':
        for classe in animais[1][1:]:
            break
        if terceiroInput == 'hematofago':
            for alimentacao in animais[1][1:][0:]:
                print(alimentacao[1:][0][1][0])
                break
        elif terceiroInput == 'herbivoro':
            for alimentacao in animais[1][1:][0:]:
                print(alimentacao[1:][1][1][0])
                break
    elif segundoInput == 'anelideo':
        for classe in animais[1][1:][1:]:
            break
        if terceiroInput == 'hematofago':
            for alimentacao in animais[1][1:][1:]:
                print(alimentacao[0:][1][1][0])
                break
        elif terceiroInput == 'onivoro':
            for alimentacao in animais[1][1:][1:]:
                print(alimentacao[1:][1][1][0])
                break


