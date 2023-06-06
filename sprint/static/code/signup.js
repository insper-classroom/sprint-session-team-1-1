// Código para esconder os campos Outro Genero e Outra Cor/Raça até que a opção "Outro" seja selecionada.
// Feito com a ajuda de um veterano
document.addEventListener('DOMContentLoaded', function() {
  const generoSelect = document.querySelector('#id_genero');
  const outroGeneroField = document.querySelector('#id_outro_genero');
  const corOuRacaSelect = document.querySelector('#id_cor_ou_raca');
  const outraCorOuRacaField = document.querySelector('#id_outra_cor_ou_raca');
  const pais = document.querySelector('#id_pais_atual');
  const estados = document.querySelector('#id_estado_atual');
  const cidade = document.querySelector('#id_cidade_atual');
  const cidade_fora = document.querySelector('#id_cidade_fora_atual');

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


  // Faz as mesmas coisas das funções acimas, porem para campos diferentes. Dessa vez feitas sozinas com base no que ja tinha sido feito
  function toggleEstado() {
    if (pais.value === 'Brasil') {
      estados.required = true;
      estados.style.display = '';
      estados.parentElement.previousElementSibling.style.display = '';
      estados.parentElement.parentElement.style.display = '';

    } else {
      estados.required = false;
      estados.style.display = 'none';
      estados.parentElement.previousElementSibling.style.display = 'none';
      estados.parentElement.parentElement.style.display = 'none';

      estados.value = '';
    }
  }

  function toggleCidadeAtual() {
    if (estados.value !== '') {
      cidade.style.display = '';
      cidade.parentElement.previousElementSibling.style.display  = '';
      cidade.parentElement.parentElement.style.display  = '';

    } else {
      cidade.style.display = 'none';
      cidade.parentElement.previousElementSibling.style.display  = 'none';
      cidade.parentElement.parentElement.style.display  = 'none';

    }
  }

  function toggleCidadeFora() {
    if (pais.value !== 'Brasil') {
      cidade_fora.style.display = '';
      cidade_fora.parentElement.previousElementSibling.style.display  = '';
      cidade.style.display = 'none';
      cidade.parentElement.previousElementSibling.style.display  = 'none';
    } else {
      cidade_fora.style.display = 'none';
      cidade_fora.parentElement.previousElementSibling.style.display  = 'none';
      cidade.style.display = '';
      cidade.parentElement.previousElementSibling.style.display  = '';
    }
  }

  toggleOutroGenero();
  toggleOutraCorOuRaca();
  toggleEstado();
  toggleCidadeAtual();
  toggleCidadeFora();

  generoSelect.addEventListener('change', toggleOutroGenero);
  corOuRacaSelect.addEventListener('change', toggleOutraCorOuRaca);
  pais.addEventListener('change', function() {
    toggleEstado();
    toggleCidadeFora();
  });
  estados.addEventListener('change', toggleCidadeAtual);
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

// Obtém as referências para as divs
const dadospessoais = document.getElementById('dadospessoais');
const dadosgeograficos = document.getElementById('dadosgeograficos');
const dadosprofissionais = document.getElementById('dadosprofissionais');
const dadosfinanceiros = document.getElementById('dadosfinanceiros');
const show_dados_pessoais = document.getElementById('show_dados_pessoais');
const show_dados_geograficos = document.getElementById('show_dados_geograficos');
const show_dados_profissionais = document.getElementById('show_dados_profissionais');
const show_dados_financeiros = document.getElementById('show_dados_financeiros');

// Define o estilo da div dadospessoais para 'block' (aparecendo)
dadospessoais.style.display = 'block';

// Define o estilo da div dadosgeograficos para 'none' (escondida)
dadosgeograficos.style.display = 'none';

// Define o estilo da div dadosprofissionais para 'none' (escondida)
dadosprofissionais.style.display = 'none';

// Define o estilo da div dadosfinanceiros para 'none' (escondida)
dadosfinanceiros.style.display = 'none';

function dados_pessoais_show() {
  dadospessoais.style.display = 'block';
  dadosgeograficos.style.display = 'none';
  dadosprofissionais.style.display = 'none';
  dadosfinanceiros.style.display = 'none';
}

function dados_geograficos_show() {
  dadospessoais.style.display = 'none';
  dadosgeograficos.style.display = 'block';
  dadosprofissionais.style.display = 'none';
  dadosfinanceiros.style.display = 'none';
}

function dados_profissionais_show() {
  dadospessoais.style.display = 'none';
  dadosgeograficos.style.display = 'none';
  dadosprofissionais.style.display = 'block';
  dadosfinanceiros.style.display = 'none';
}

function dados_financeiros_show() {
  dadospessoais.style.display = 'none';
  dadosgeograficos.style.display = 'none';
  dadosprofissionais.style.display = 'none';
  dadosfinanceiros.style.display = 'block';
}

var input = document.getElementById("id_nome");
input.setAttribute('placeholder', 'Insira seu primeiro nome');

var input = document.getElementById("id_sobrenome");
input.setAttribute('placeholder', 'Insira seu sobrenome');

var input = document.getElementById("id_username");
input.setAttribute('placeholder', 'Insira seu nome de exibição');

var input = document.getElementById("id_password1");
input.setAttribute('placeholder', 'Insira sua senha');

var input = document.getElementById("id_password2");
input.setAttribute('placeholder', 'Confirme sua senha');

var input = document.getElementById("id_email");
input.setAttribute('placeholder', 'Insira seu e-mail');

var input = document.getElementById("id_telefone");
input.setAttribute('placeholder', 'Insira seu telefone');

var input = document.getElementById("id_cpf");
input.setAttribute('placeholder', 'Insira seu CPF');

var input = document.getElementById("id_rg");
input.setAttribute('placeholder', 'Insira seu RG');

var input = document.getElementById("id_linkedin");
input.setAttribute('placeholder', 'Insira seu LinkedIn');

var input = document.getElementById("id_curso");
input.setAttribute('placeholder', 'Insira seu curso');

var input = document.getElementById("id_formatura");
input.setAttribute('placeholder', 'Insira seu ano de formatura');

var input = document.getElementById("id_ingresso");
input.setAttribute('placeholder', 'Insira seu ano de ingresso');

var input = document.getElementById("id_outra_cor_ou_raca");
input.setAttribute('placeholder', 'Insira sua cor/raça');

var input = document.getElementById("id_outro_genero");
input.setAttribute('placeholder', 'Insira seu gênero');








