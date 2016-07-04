var functionRegistry = {}

var makeButton = function(x, y, w, h, r, g, b, bind, args){
	fill(r, g, b);
	rect(x, y, w, h);
	functionRegistry[(x,y,x+w,y+h)] = (bind, args);
	
mouseClicked = function(){
	var limits = functionRegistry.keys();
	for (var ind = 0; ind<limits.length; ind++){
		limit = limits[ind];
		if ((limit[2]>=mouseX>=limit[0]) && (limit[3]>=mouseY>=limit[1])){
			functionRegistry[limit][0](functionRegistry[limit][1]);
		}
