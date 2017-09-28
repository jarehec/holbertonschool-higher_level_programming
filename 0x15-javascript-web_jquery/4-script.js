// toggle the class of the HEADER tag when DIV#redheader is clicked
$('DIV#toggle_header').click(function () {
  if ($('HEADER').attr('class') === 'green') {
    $('HEADER').attr('class', 'red');
  } else { $('HEADER').attr('class', 'green'); }
});
