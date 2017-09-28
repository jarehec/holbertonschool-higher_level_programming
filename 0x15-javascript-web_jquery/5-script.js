// adds a LI element to UL.my_list when DIV#add_item is clicked
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
