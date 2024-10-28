
certo=False
velocidade_permitida=80
iniciar=input("deseja iniciar, s para sim ou n para não: ")
if iniciar == "n":
    print("fechando sistema")
    certo=True
    
while certo==False and iniciar =="s":
    
    velocidade_motorista=int(input("sua velocidade:  "))
    if velocidade_motorista <0:
      print("sistema parado")
      break

      
    if velocidade_motorista <= velocidade_permitida:
      print("sem multa")

      
    elif velocidade_motorista>velocidade_permitida and velocidade_motorista<= velocidade_permitida +10:
      print("voce recebeu uma multa leve")

      


    elif velocidade_motorista> velocidade_permitida +10 and velocidade_motorista<= velocidade_permitida+20:
      print("voce recebeu um multa grave")

  



    elif velocidade_motorista>velocidade_permitida +20 and velocidade_motorista<= velocidade_permitida +999:
      print("voce recebeu uma multa gravissima")

        