
// funcion que para buscar posts del blog
$('#search').keyup(function(e)) {
  consulta = $('#search').val();
  $.ajax({
    data: {'nombre': consulta},
    url: '/blog/buscar/',
    type: 'get',
    success: function(data) {
      console.log(data[0].nombre);
    },
    error: function(messagge) {
      console.log(messages);
    }
  });
});
