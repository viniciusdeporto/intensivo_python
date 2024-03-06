livros = ["dogma e ritual da alta magia", "isis sem veu", "doutrina secreta", "neuromancer", "a divina comedia", "biblia", "o cabalion"]
print(f"dos livros que estou lendo, vale ressaltar que a {livros[-2].title()} contem quase todos dentro dele")
livros.append("dicionario dos simbolos")
print(livros)
livros.insert(2, "a chave dos grandes misterios")
print(livros)
del livros[4]
print(livros)
ultimo_livro = livros.pop()
print(f"Ultimo livro que comprei foi {livros[-1].title()}")
livros.remove("a divina comedia")
print(livros)
n_p_r = "o cabalion"
livros.remove(n_p_r)
print(livros)
# Ordenar a lista permanentemente
livros.sort()
print(livros)
# ordenar em ordme alfabetica ao inverso
livros.sort(reverse=True)
print(livros)
print("\nAqui está uma lista temporariamente ordenada:")
print(sorted(livros))
livros.reverse()
print(livros)