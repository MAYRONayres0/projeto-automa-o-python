from datetime import datetime


def obter_nome():
    while True:
        
            nome=input("seu nome ")

            if not nome.strip():
                print("vc esqueceu seu nome")

            else:
                return nome
        

def obter_ano():
     while True:
        try:
                 
                ano_nascimento=input("ano de nascimento ")

                if not ano_nascimento.strip():
                    print("vc esqueceu de preencher o ano")
                    continue

                ano_nascimento=int(ano_nascimento)

                ano_atual=datetime.now().year
                if ano_nascimento >ano_atual:
                    print("o ano deve ser menor que o ano atual")
                    continue
                return ano_nascimento
        except ValueError:
                print("por favor insira um ano valido, menor que o atual")


    





          
def main():
    while True:
        nome=obter_nome()
        ano_nascimento=obter_ano()
       


       

        ano_atual=datetime.now().year


        idade = ano_atual - ano_nascimento

        

        print(f"olá {nome}, vc tem {idade} anos de idade.")
        break
main()