<!DOCTYPE html>
<html>

<link rel="stylesheet" href="${pageContext.request.contextPath}/css/map.css" />
<script src="js/jquery.min.js"></script>
<script src="js/map.js"></script>
<script src="js/custom.js"></script>
<script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBJH1z6tSH9ZyCURsi7-uEN66FMa_WEQWI&libraries=visualization&callback=initMap"></script>

<head>
	<meta charset="utf-8">
	<title>Heatmap</title>
</head>

<body>
<div class="row">

<div id="header">
	<h1 id="main-header">&nbsp;Fomono</h1>
</div>
<div class="column main-left">
	<div id="toggle-heatmap">
		<button onclick="toggleHeatmap()">Toggle Heatmap</button>
<!-- 		<button onclick="changeGradient()">Change gradient</button> -->
<!-- 		<button onclick="changeRadius()">Change radius</button> -->
<!-- 		<button onclick="changeOpacity()">Change opacity</button> -->
	</div>
	<div id="map"></div>
</div>
		<div class="column main-right">
			<div class="row">
				<div class="column left row-label label-white">&nbsp;Filter</div>
				<div class="column right row-label label-grey">&nbsp;Trending</div>
			</div>
			<div class="row row-label label-blue">&nbsp;Location</div>
			<div class="row row-label label-grey">&nbsp;City/Zip</div>
			<div class="row row-label label-blue">&nbsp;Category</div>
			<div class="row" id="radio-button-container">
				<div class="radio">
					<input id="radio-sports" name="topic-rb" type="radio" value="sports" checked>
					<label for="radio-sports" class="radio-label">Sports</label>
				</div>

				<div class="radio">
					<input id="radio-entertainment" name="topic-rb" type="radio" value="entertainment">
					<label for="radio-entertainment" class="radio-label">Entertainment</label>
				</div>

				<div class="radio">
					<input id="radio-music" name="topic-rb" type="radio" value="music"> <label
						for="radio-music" class="radio-label">Music</label>
				</div>

				<div class="radio">
					<input id="radio-information" name="topic-rb" type="radio" value="information">
					<label for="radio-information" class="radio-label">Information</label>
				</div>

				<div class="radio">
					<input id="radio-politics" name="topic-rb" type="radio" value="politics"> <label
						for="radio-politics" class="radio-label">Politics</label>
				</div>

				<div class="radio">
					<input id="radio-emergency" name="topic-rb" type="radio" value="emergency">
					<label for="radio-emergency" class="radio-label">Emergency</label>
				</div>
			</div>
		</div>
	</div>
</body>
<h1>Footer</h1>
</html>
