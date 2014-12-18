$(document).ready(function() {

	var current = $("#search-form").find("#search-input").val();
	console.log(current);

  var suggestions = [
    { value: 'show IT', data: 'to'  },
    { value: 'data from database', data: 'place' },
    { value: 'from place to input', data: 'input' },
  ];

  // setup autocomplete function pulling from currencies[] array
  $('#search-input').autocomplete({
    source: "http://localhost:8000/sms/route",
    delay: 500
  });

  $('#search-form').on('submit', function(event) {
    event.preventDefault();
    searchPlace();
  });

 	function searchPlace() {
    var dataArray = $('#search-form').serializeArray();
    var data = {};

    for (var i = 0; i < dataArray.length; i++) {
      data[dataArray[i]['name']] = dataArray[i]['value'];
    };

    $.get("http://localhost:8000/sms/map", data)
    .done(function(data) {
      $('#search-alert').addClass('hidden');
      alert(data['dest'] + data['src'] + data['path'])
    })
    .fail(function(data) {
      // Append the response's error text to the alert element
      $('#search-alert').removeClass('hidden');
    });

  }

});