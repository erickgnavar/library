$(document).on('ready', function (){
	$('#form-login').on('submit', function (e){
		e.preventDefault();
		$(this).submit(function (data){
			console.log(data);
		});
	});
});