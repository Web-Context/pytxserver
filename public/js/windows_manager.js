Array.prototype.last = function() {
	return this[this.length-1];
}
var WindowsManager = {
	focusOnWindow: new Array(),
	index: 0,
	show: function(id){
		$(id).show();
		this.focusOnWindow.push(id);
		this.index++;
	},
	popHide: function(){
		var focus = this.focusOnWindow.pop();
		$(focus).hide();
		this.index --;
	}
}
