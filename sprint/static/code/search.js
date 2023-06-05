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
    "filtro-ano-formatura",
    "filtro-ano-inicial",
    "filtro-ano-final",
  ];
  
  filtrosIds.forEach(function(id) {
    var filtro = document.getElementById(id);
    var placeholder = id.replace('filtro-', '')
    filtro.setAttribute('placeholder', placeholder);
    filtro.style.margin = '5px';
  });
  

//   Regex feito pelo ChatGPT para auto-formatar alguns dos campos de filtros

// Auto-format for ID (accepts only numbers)
const idInput = document.getElementById("filtro-id");
idInput.addEventListener("input", () => {
  idInput.value = idInput.value.replace(/\D/g, "");
});

// Auto-format for CPF (11 numbers with formatting, limited to 11 characters)
const cpfInput = document.getElementById("filtro-cpf");
cpfInput.addEventListener("input", () => {
  cpfInput.value = cpfInput.value
    .replace(/\D/g, "")
    .slice(0, 11)
    .replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4");
});

// Auto-format for RG (9 numbers with formatting, limited to 9 characters)
const rgInput = document.getElementById("filtro-rg");
rgInput.addEventListener("input", () => {
  rgInput.value = rgInput.value
    .replace(/\D/g, "")
    .slice(0, 9)
    .replace(/(\d{2})(\d{3})(\d{3})(\d{1})/, "$1.$2.$3-$4");
});

// Auto-format for numero (13 numbers with formatting, limited to 13 characters)
const numeroInput = document.getElementById("filtro-numero");
numeroInput.addEventListener("input", () => {
  numeroInput.value = numeroInput.value
    .replace(/\D/g, "")
    .slice(0, 13)
    .replace(/(\d{2})(\d{2})(\d{5})(\d{4})/, "+$1 ($2) $3.$4");
});

// Auto-format for ano_nascimento, ano_matricula, and ano_formatura (4 numbers, limited to 4 characters)
const yearInputs = document.querySelectorAll(
  ".filtro-ano-nascimento, .filtro-ano-matricula, .filtro-ano-formatura"
);
yearInputs.forEach((input) => {
  input.addEventListener("input", () => {
    input.value = input.value.replace(/\D/g, "").slice(0, 4);
  });
});

// Auto-format for ano_inicial (4 numbers, limited to 4 characters)
const anoInicialInput = document.getElementById("filtro-ano-inicial");
anoInicialInput.addEventListener("input", () => {
  anoInicialInput.value = anoInicialInput.value.replace(/\D/g, "").slice(0, 4);
});

// Auto-format for ano_final (4 numbers, limited to 4 characters)
const anoFinalInput = document.getElementById("filtro-ano-final");
anoFinalInput.addEventListener("input", () => {
  anoFinalInput.value = anoFinalInput.value.replace(/\D/g, "").slice(0, 4);
});