document.addEventListener('DOMContentLoaded', function() {
  const generoSelect = document.querySelector('#id_genero');
  const outroGeneroField = document.querySelector('#id_outro_genero');
  const corOuRacaSelect = document.querySelector('#id_cor_ou_raca');
  const outraCorOuRacaField = document.querySelector('#id_outra_cor_ou_raca');

  function toggleOutroGenero() {
    if (generoSelect.value === 'Outro') {
      outroGeneroField.required = true;
      outroGeneroField.style.display = '';
      outroGeneroField.previousElementSibling.style.display = '';
    } else {
      outroGeneroField.required = false;
      outroGeneroField.style.display = 'none';
      outroGeneroField.previousElementSibling.style.display = 'none';
      outroGeneroField.value = '';
    }
  }

  function toggleOutraCorOuRaca() {
    if (corOuRacaSelect.value === 'Outra') {
      outraCorOuRacaField.required = true;
      outraCorOuRacaField.style.display = '';
      outraCorOuRacaField.previousElementSibling.style.display = '';
    } else {
      outraCorOuRacaField.required = false;
      outraCorOuRacaField.style.display = 'none';
      outraCorOuRacaField.previousElementSibling.style.display = 'none';
      outraCorOuRacaField.value = '';
    }
  }

  toggleOutroGenero();
  toggleOutraCorOuRaca();

  generoSelect.addEventListener('change', toggleOutroGenero);
  corOuRacaSelect.addEventListener('change', toggleOutraCorOuRaca);
});
