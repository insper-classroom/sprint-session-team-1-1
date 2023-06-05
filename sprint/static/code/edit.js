// Mesmo código utilizado no signup.js
document.addEventListener('DOMContentLoaded', function() {
    const generoSelect = document.querySelector('#id_genero');
    const outroGeneroField = document.querySelector('#id_outro_genero');
    const pais = document.querySelector('#id_pais_atual');
    const estados = document.querySelector('#id_estado_atual');
    const cidade = document.querySelector('#id_cidade_atual');
    const cidade_fora = document.querySelector('#id_cidade_fora_atual');
  
    function toggleOutroGenero() {
      if (generoSelect.value === 'Outro') {
        outroGeneroField.required = true;
        outroGeneroField.style.display = '';
        outroGeneroField.parentElement.previousElementSibling.style.display = ''; //Exibe o botão se o valor do seletor genero for outro
      } else {
        outroGeneroField.required = false;
        outroGeneroField.style.display = 'none';
        outroGeneroField.parentElement.previousElementSibling.style.display = 'none'; //Esconde o botao se o valor selecionado não for outro
        outroGeneroField.value = '';
      }
    }
  
    // Faz as mesmas coisas das funções acimas, porem para campos diferentes. Dessa vez feitas sozinas com base no que ja tinha sido feito
    function toggleEstado() {
      if (pais.value === 'Brasil') {
        estados.required = true;
        estados.style.display = '';
        estados.parentElement.previousElementSibling.style.display = '';
      } else {
        estados.required = false;
        estados.style.display = 'none';
        estados.parentElement.previousElementSibling.style.display = 'none';
        estados.value = '';
      }
    }
  
    function toggleCidadeAtual() {
      if (estados.value !== '') {
        cidade.style.display = '';
        cidade.parentElement.previousElementSibling.style.display = '';
      } else {
        cidade.style.display = 'none';
        cidade.parentElement.previousElementSibling.style.display = 'none';
      }
    }
  
    function toggleCidadeFora() {
      if (pais.value !== 'Brasil') {
        cidade_fora.style.display = '';
        cidade_fora.parentElement.previousElementSibling.style.display = '';
        cidade.style.display = 'none';
        cidade.parentElement.previousElementSibling.style.display = 'none';
      } else {
        cidade_fora.style.display = 'none';
        cidade_fora.parentElement.previousElementSibling.style.display = 'none';
        cidade.style.display = '';
        cidade.parentElement.previousElementSibling.style.display = '';
      }
    }
  
    toggleOutroGenero();
    toggleEstado();
    toggleCidadeAtual();
    toggleCidadeFora();
  
    generoSelect.addEventListener('change', toggleOutroGenero);
    pais.addEventListener('change', function() {
      toggleEstado();
      toggleCidadeFora();
    });
    estados.addEventListener('change', toggleCidadeAtual);
  });

  // Código para auto formatar os campos RG, e Telefone dor formulario de inscrição.
// Feito com ajuda de um veterano (e do GPT para fazer os regex)
const telefone = document.querySelector('#id_telefone');
const rg = document.querySelector('#id_rg');
const formatura = document.querySelector('#id_formatura');

telefone.addEventListener('input', formataTelefone);
rg.addEventListener('input', formataRG);
formatura.addEventListener('input', function() { formataAnos('id_formatura'); });

function formataTelefone() {
  let digito = telefone.value.replace(/\D/g, '');
  digito = digito.replace(/^(\d{2})(\d{2})(\d{5})(\d{4})$/, '+$1 ($2) $3.$4');
  telefone.value = digito;
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
