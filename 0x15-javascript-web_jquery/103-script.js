const url = 'https://www.fourtonfish.com/hellosalut/hello/';

$('document').ready(function () {
  $('#btn_translate').click(translation);
  $('#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        translation();
      }
    });
  });
});

function translation () {
  $.get(url + $.param({ lang: $('#language_code').val() }), function (data) {
    $('#hello').html(data.hello);
  });
}
