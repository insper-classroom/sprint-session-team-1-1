var input = document.getElementById("busca-nome");
input.setAttribute('placeholder', 'Nome');

var input = document.getElementById("busca-sobrenome");
input.setAttribute('placeholder', 'Sobrenome');

var input = document.getElementById("busca-exibicao");
input.setAttribute('placeholder', 'Nome de Exibição');


// Código gambiarra para me poupar de fazer manualmente cada placeholder, tava cansado
var filtrosIds = [
    "filtro-id",
    "filtro-cpf",
    "filtro-rg",
    "filtro-email",
    "filtro-numero",
    "filtro-curso",
    "filtro-estado-nascimento",
    "filtro-estado-atual",
    "filtro-cidade-nascimento",
    "filtro-cidade-atual",
    "filtro-pais-atual",
    "filtro-ano-nascimento",
    "filtro-ano-matricula",
    "filtro-ano-formatura"
  ];
  
  filtrosIds.forEach(function(id) {
    var filtro = document.getElementById(id);
    var placeholder = id.replace('filtro-', '')
    filtro.setAttribute('placeholder', placeholder);
    filtro.style.margin = '5px';
  });
  