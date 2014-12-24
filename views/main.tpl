<!DOCTYPE html>
<html>
<head>
	<meta charset='utf-8' />
	<title>{{page_title}}</title>
	<link rel="stylesheet" type="text/css" href="/public/css/github.css" />
	<link rel="stylesheet" type="text/css" href="/public/css/doc.css" />
	<link rel="stylesheet" type="text/css" href="/public/css/games.css" />
	<script type="text/javascript" src="/public/js/jquery-1.11.2.min.js"></script>
	<script type="text/javascript" src="/public/js/windows_manager.js"></script>
</head>
<body>
	% include('header.html')
	<aside class="menu">
		<h2>Game Platforms</h2>
		<ul>
			% for platformitem in platforms:
			<li><a 
				%if platform and platform['code'] == platformitem['code'] :
				class="active" 
				%end 
				href="/games/{{platformitem['code']}}">{{platformitem['name']}}</a></li>
				% end
			</ul>
			% if games : 
			<h2>Games</h2>
			% end
			<ul>
				% for gameitem in games : 
				<li><a 
					%if game and game['id'] == gameitem['id'] :
					class="active" 
					%end 
					href="/game/{{gameitem['id']}}" title="Show the game '{{gameitem['title']}}'">{{gameitem['title']}}</a></li>
					% end
				</ul>
			</aside>
			<div class="container">
				<div id="markup">
					<article id="content" class="markdown-body">{{!base}}</article>
				</div>
			</div>
			% include('footer.html')			
			% include('login_form.html')

			<script type="text/javascript">
			$(window).ready(function(){
				var windows = WindowsManager; 
				$('#search').keypress(function(event){
					if(event.which == 13){
						$.get( "/games/search/"+$('#search').val(), function( response ) {
    				console.log( response ); // server response
    			});
					}
				});
				$('#login').click(function(){
					windows.show('#login-form');
				});
				$('#prefs').click(function(){
					alert('Preferences');
				});

				// by default hide all forms. 
				$('.form').hide();
				$(document).keydown(function(e){
					var code = e.keyCode ? e.keyCode : e.which;
					if(code == 27){
						windows.popHide();
					}
				});

			});
			</script>
		</body>
		</html>
