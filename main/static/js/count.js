const targetForm = document.querySelector('.jss_content_form');
targetForm.addEventListener('keyup', () => {
  document.querySelector('.counted_text').innerHTML = targetForm.value.length;
});
