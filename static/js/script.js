$(document).ready(function(){

	var API_URL = 'api/code-analyze';
	$('#source-code-sumbit').on('click', ()=> {
		var sourceCode = $('#source-code').val();
		if(!sourceCode) return;
		let formData = new FormData();
		formData.append('csrf_token', $('meta[name="csrf-token"]').attr('content'));
		formData.append('source_code', sourceCode);
		$.ajax({
			url: API_URL,
			type: 'POST',
			data: formData,
			processData: false,
			contentType: false,
			success: function(response, status, xhr){
				if(response.errors && response.errors.length){
					$('#results-block').html(getSourceCodeError(response.errors, sourceCode));
				}else{
					$('#results-block').html('<div class="text-center no-errors">No Errors !</div>');
				}
			},
			error: function(response_status){
				console.log('ERROR' + response_status);
			},
		});
	});

});

function getSourceCodeError(errorList, sourceCode){
	let sourceCodeList = sourceCode.split('\n');
	var formattedString = `<h2>Errors: </h2>`;
	$.each(errorList, (idx, elem) => {
		let srcText = sourceCodeList[parseInt(elem.line)-1];
		formattedString += `<div class="errors">
								<div class="src-text">
									<span class="line-num">Line Num ${elem.line}: </span>
									<span class="src-text">${srcText}</span>
								</div>
								<div class="err-msg">
									<span class="err-id">${elem.message_id}: </span>
									<span>${elem.message}</span>
								</div>
							</div>`;
	});
	return formattedString;
}