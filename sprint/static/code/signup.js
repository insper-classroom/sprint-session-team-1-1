// Código para esconder os campos Outro Genero e Outra Cor/Raça até que a opção "Outro" seja selecionada.
// Feito com a ajuda de um veterano
document.addEventListener('DOMContentLoaded', function() {
  const generoSelect = document.querySelector('#id_genero');
  const outroGeneroField = document.querySelector('#id_outro_genero');
  const corOuRacaSelect = document.querySelector('#id_cor_ou_raca');
  const outraCorOuRacaField = document.querySelector('#id_outra_cor_ou_raca');

  function toggleOutroGenero() {
    if (generoSelect.value === 'Outro') {
      outroGeneroField.required = true;
      outroGeneroField.style.display = '';
      outroGeneroField.previousElementSibling.style.display = ''; //Exibe o botão se o valor do seletor genero for outro
    } else {
      outroGeneroField.required = false;
      outroGeneroField.style.display = 'none';
      outroGeneroField.previousElementSibling.style.display = 'none'; //Esconde o botao se o valor selecionado não for outro
      outroGeneroField.value = '';
    }
  }

  function toggleOutraCorOuRaca() {
    if (corOuRacaSelect.value === 'Outra') {
      outraCorOuRacaField.required = true;
      outraCorOuRacaField.style.display = '';
      outraCorOuRacaField.previousElementSibling.style.display = ''; //Exibe o botão se o valor do seletor genero for outro
    } else {
      outraCorOuRacaField.required = false;
      outraCorOuRacaField.style.display = 'none';
      outraCorOuRacaField.previousElementSibling.style.display = 'none'; //Esconde o botao se o valor selecionado não for outro
      outraCorOuRacaField.value = '';
    }
  }

  toggleOutroGenero();
  toggleOutraCorOuRaca();

  //Adiciona os event listenes para monitorar interações no HTML
  generoSelect.addEventListener('change', toggleOutroGenero);
  corOuRacaSelect.addEventListener('change', toggleOutraCorOuRaca);
});


// Código para auto formatar os campos RG, CPF e Telefone dor formulario de inscrição.
// Feito com ajuda de um veterano (e do GPT para fazer os regex)
const telefone = document.querySelector('#id_telefone');
const cpf = document.querySelector('#id_cpf');
const rg = document.querySelector('#id_rg');
const ingresso = document.querySelector('#id_ingresso');
const formatura = document.querySelector('#id_formatura');

telefone.addEventListener('input', formataTelefone);
cpf.addEventListener('input', formataCPF);
rg.addEventListener('input', formataRG);
ingresso.addEventListener('input', function() { formataAnos('id_ingresso'); });
formatura.addEventListener('input', function() { formataAnos('id_formatura'); });

function formataTelefone() {
  let digito = telefone.value.replace(/\D/g, '');
  digito = digito.replace(/^(\d{2})(\d{2})(\d{5})(\d{4})$/, '+$1 ($2) $3.$4');
  telefone.value = digito;
}

function formataCPF() {
  let digito = cpf.value.replace(/\D/g, '');
  digito = digito.replace(/(\d{3})(\d)/, '$1.$2');
  digito = digito.replace(/(\d{3})(\d)/, '$1.$2');
  digito = digito.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
  cpf.value = digito;
}

function formataRG() {
  let digito = rg.value.replace(/\D/g, '');
  digito = digito.replace(/(\d{2})(\d)/, '$1.$2');
  digito = digito.replace(/(\d{3})(\d)/, '$1.$2');
  digito = digito.replace(/(\d{3})(\d{1})$/, '$1-$2');
  rg.value = digito;
}

function formataAnos(fieldId) {
  const caixa_ano = document.querySelector(`#${fieldId}`);
  if (caixa_ano.value.length > 4) {
    caixa_ano.value = caixa_ano.value.slice(0, 4);
  }
}