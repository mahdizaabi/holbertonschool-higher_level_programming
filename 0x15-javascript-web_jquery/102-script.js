$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $.get(('https://fourtonfish.com/hellosalut/?lang=' +
         $('#language_code').val()), function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
