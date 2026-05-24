nome_do_usuario = input()
perfil_escolhido = input()
perfis_disponiveis = ["admin", "Admin", "editor", "Editor", "Visualizador","visualizador"]
if nome_do_usuario == "":
    print("[ ERRO ] nome não pode ser vazio")
if perfil_escolhido not in perfis_disponiveis:
    print("[ ERRO ] perfil inválido")
else:
    print("Cadastro do usuário do usuário confirmado")
