const url = 'https://www.fourtonfish.com/hellosalut/hello/';

$('document').ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
