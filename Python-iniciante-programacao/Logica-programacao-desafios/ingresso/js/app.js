function comprar() {
    let tipo = document.getElementById('tipo-ingresso').value;
    let qtd = parseInt(document.getElementById('qtd').value);

    // 1- Adicione uma verificação para garantir que a quantidade inserida pelo usuário seja um número positivo. 
    // Se o valor não for válido, exiba uma mensagem de erro adequada.
    if (isNaN(qtd) || qtd <= 0) {
        alert('Inserira um valor positivo!');
        return;
    }

    // 2- Crie uma função que aceite uma string como parâmetro, 
    // utilize a função parseInt para converter essa string em um número inteiro e retorne o resultado.
    let valor = '';
    resultado(valor, qtd);

    if (tipo == 'pista') {
        comprarPista(qtd);
        } else if (tipo == 'superior') {
            comprarSuperior(qtd);
        }
    else {
        comprarInferior(qtd);
    }
}

function comprarPista(qtd) {
    let qtdPista = parseInt(document.getElementById('qtd-pista').textContent);
    if (qtd > qtdPista) {
        alert('Quantidade indisponível para tipo pista');
    } else {
        qtdPista -= qtd;
        document.getElementById('qtd-pista').textContent = qtdPista;
        alert('Compra realizada com sucesso!');
    }
}

function comprarSuperior(qtd) {
    let qtdSuperior = parseInt(document.getElementById('qtd-superior').textContent);
    if (qtd > qtdSuperior) {
        alert('Quantidade indisponível para tipo pista');
    } else {
        qtdSuperior -= qtd;
        document.getElementById('qtd-superior').textContent = qtdSuperior;
        alert('Compra realizada com sucesso!');
    }
}

function comprarInferior(qtd) {
    let qtdInferior = parseInt(document.getElementById('qtd-inferior').textContent);
    if (qtd > qtdInferior) {
        alert('Quantidade indisponível para tipo pista');
    } else {
        qtdInferior -= qtd;
        document.getElementById('qtd-inferior').textContent = qtdInferior;
        alert('Compra realizada com sucesso!');
    }
}

function resultado(valor, qtd){
    valor = qtd
    valor = parseInt(valor)
    return alert(valor);
}