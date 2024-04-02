def escrever_dados_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        for cliente in dados:
            linha = ','.join(cliente)
            arquivo.write(linha + '\n')

clientes = [
    ["João Silva", "Rua dos Flores, 123, Cidade, Estado", "joao.silva@example.com", "123.456.789-00"],
    ["Maria Santos", "Avenida das Palmeiras, 456, Cidade, Estado", "maria.santos@example.com", "987.654.321-00"],
    ["Pedro Oliveira", "Rua das Acácias, 789, Cidade, Estado", "pedro.oliveira@example.com", "456.789.123-00"],
    ["Ana Souza", "Avenida dos Ipês, 321, Cidade, Estado", "ana.souza@example.com", "321.654.987-00"],
    ["Carlos Rodrigues", "Rua das Oliveiras, 987, Cidade, Estado", "carlos.rodrigues@example.com", "654.987.321-00"],
    ["Camila Costa", "Avenida das Rosas, 654, Cidade, Estado", "camila.costa@example.com", "789.123.456-00"],
    ["Rafaela Pereira", "Rua das Violetas, 147, Cidade, Estado", "rafaela.pereira@example.com", "852.963.741-00"],
    ["Luiz Almeida", "Avenida das Orquídeas, 258, Cidade, Estado", "luiz.almeida@example.com", "369.258.147-00"],
    ["Isabela Santos", "Rua dos Cravos, 369, Cidade, Estado", "isabela.santos@example.com", "741.852.963-00"],
    ["Gabriel Lima", "Avenida das Tulipas, 741, Cidade, Estado", "gabriel.lima@example.com", "963.852.741-00"],
    ["Larissa Costa", "Rua das Margaridas, 852, Cidade, Estado", "larissa.costa@example.com", "147.369.258-00"],
    ["Thiago Fernandes", "Avenida das Azaleias, 963, Cidade, Estado", "thiago.fernandes@example.com", "258.741.369-00"],
    ["Júlia Pereira", "Rua dos Lírios, 147, Cidade, Estado", "julia.pereira@example.com", "369.147.741-00"],
    ["Lucas Oliveira", "Avenida das Camélias, 852, Cidade, Estado", "lucas.oliveira@example.com", "741.369.147-00"],
    ["Beatriz Rodrigues", "Rua das Hortênsias, 963, Cidade, Estado", "beatriz.rodrigues@example.com", "147.741.369-00"],
    ["Matheus Almeida", "Avenida das Gérberas, 369, Cidade, Estado", "matheus.almeida@example.com", "369.741.147-00"],
    ["Amanda Souza", "Rua das Camélias, 741, Cidade, Estado", "amanda.souza@example.com", "741.147.369-00"],
    ["Gustavo Lima", "Avenida das Margaridas, 147, Cidade, Estado", "gustavo.lima@example.com", "147.369.741-00"],
    ["Sofia Costa", "Rua dos Girassóis, 741, Cidade, Estado", "sofia.costa@example.com", "369.741.147-00"],
    ["Enzo Fernandes", "Avenida das Orquídeas, 369, Cidade, Estado", "enzo.fernandes@example.com", "741.147.369-00"],
]

nome_arquivo = "clientes.txt"
escrever_dados_arquivo(nome_arquivo, clientes)
