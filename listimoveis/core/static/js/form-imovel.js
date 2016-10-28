/****************************************************************************************************************************************/
var oForm = {
	jqThis : null
	
	, Carregar: function () {
		var _this = this;

		_this.jqThis = $('#jqForm');
		if (_this.jqThis.length){             
			_this.CarregarEventos();
		}
	}
	, CarregarEventos: function () {
		var _this = this;
		$('.jqName').on('change' , function () { _this.SlugName(this);});
	}
	, SlugName: function () {
		var name = $('.jqName').val(),
			input = $('#id_slug'),
			slug = '',
			trimmed = '';

		trimmed = $.trim(name);
		slug = trimmed.replace(/[^a-z0-9-]/gi, '-').
		replace(/-+/g, '-').
		replace(/^-|-$/g, '');
		var d = new Date();
		input.val(slug.toLowerCase() + d.getMilliseconds());
	}
};
/****************************************************************************************************************************************/ 
$(window).load(function () {
	oForm.Carregar();
});
/****************************************************************************************************************************************/