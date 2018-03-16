
		var map, heatmap;
		var locations = [];

		function initMap() {
			map = new google.maps.Map(document.getElementById('map'), {
				zoom : 5,
				center : {
					lat : 41.702496,
					lng : -86.239694
				},
				mapTypeId : 'satellite'
			});
			
//			heatmap = new google.maps.visualization.HeatmapLayer({
//				data : getPoints(),
//				map : map
//			});
//			
			//updateMap();
		}

		function toggleHeatmap() {
			heatmap.setMap(heatmap.getMap() ? null : map);
		}

		function changeGradient() {
			var gradient = [ 'rgba(0, 255, 255, 0)', 'rgba(0, 255, 255, 1)',
					'rgba(0, 191, 255, 1)', 'rgba(0, 127, 255, 1)',
					'rgba(0, 63, 255, 1)', 'rgba(0, 0, 255, 1)',
					'rgba(0, 0, 223, 1)', 'rgba(0, 0, 191, 1)',
					'rgba(0, 0, 159, 1)', 'rgba(0, 0, 127, 1)',
					'rgba(63, 0, 91, 1)', 'rgba(127, 0, 63, 1)',
					'rgba(191, 0, 31, 1)', 'rgba(255, 0, 0, 1)' ]
			heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);
		}

		function changeRadius() {
			heatmap.set('radius', heatmap.get('radius') ? null : 20);
		}

		function changeOpacity() {
			heatmap.set('opacity', heatmap.get('opacity') ? null : 0.2);
		}
		
		
		function getPoints() {
			$.ajax({
				url: "http://localhost:5002/getLocations", 
				type: "GET",
				dataType: 'jsonp',
				success: function(data) {
					handleData(data);
				},
				error: function (xhr, ajaxOptions, thrownError){
                    console.log(xhr.status);
                },
			});
			return locations;
		}
		
		function handleData(data) {
			locations = [];
			for (i = 0; i < data.sports.length; i++) {
				locations.push(new google.maps.LatLng(data.sports[i].lat, data.sports[i].lng));
			}
		}
		
		function updateMap(){
			setInterval(function(){
				topic = console.log($("input:radio[name='topic-rb']:checked").val());
				heatmap.setData([]);
				heatmap.setData(getPoints());
				// pass topic to getPoints, have different endpoints for the different topic
			}, 400);
		}
		