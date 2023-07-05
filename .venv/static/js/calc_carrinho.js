var n1 = document.getElementById('quantidade');
var n2 = document.getElementById('valor');


function adicionaCarrinho(nomeProduto){
    var n1 = document.getElementById('quantidade-'+nomeProduto);
    window.location.href = "/carrinho/"+nomeProduto+"/"+ n1.value;
    
}

