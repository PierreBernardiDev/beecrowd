def identificar_animal(primeiro, segundo, terceiro):
    animais = {
        "vertebrado": {
            "ave": {
                "carnivoro": "aguia",
                "onivoro": "pomba"
            },
            "mamifero": {
                "onivoro": "homem",
                "herbivoro": "vaca"
            }
        },
        "invertebrado": {
            "inseto": {
                "hematofago": "pulga",
                "herbivoro": "lagarta"
            },
            "anelideo": {
                "hematofago": "sanguessuga",
                "onivoro": "minhoca"
            }
        }
    }

    return animais.get(primeiro, {}).get(segundo, {}).get(terceiro, "Animal não encontrado")

primeiroInput = input('Insira o primeiro dado: ').strip()
segundoInput = input('Insira o segundo dado: ').strip()
terceiroInput = input('Insira o terceiro dado: ').strip()

animal = identificar_animal(primeiroInput, segundoInput, terceiroInput)
print(animal)
