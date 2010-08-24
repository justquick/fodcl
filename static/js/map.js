   var points = new Array();
    var images = new Array();
    
    images[0] = new Array(474, 478, 481, 493);
    points[0] = new Array(39.45146, -79.30930, "Deep Creek Cove", "Excessive floating pondweed growth starts in early June. By early July the cove is totally covered");
  
    points[1] = new Array(39.45236, -79.30634, "Turkey Head Point", "By early July weeds have spread around the point, creating anaerobic zone by shores. By early August, weeds die off cloging docks.");
    images[1] = new Array(487,484);
    
    images[2] = new Array(490, 496, 499, 502);
    points[2] = new Array(39.45101, -79.30396, "Unnamed Cove", "Heavy nutrients cause extensive growths by mid July.");

    points[3] = new Array(39.44986, -79.30393, "Unnamed Cove", "By August, there are algae blooms and extensive euglena masses.");
    images[3] = new Array(505, 508, 511);
    
    points[4] = new Array(39.46347, -79.30584, "Penn Cove", "Has extensive weed and algae by mid season, substantially reducing recreational use.");
    images[4] = new Array(514, 517);
    
    points[5] = new Array(39.44933, -79.31093, "Deep Creek Cove", "By late August, the cove shows water quality decline at the end of the season. Throughout the season the cove has heavy sediment flow. Is this the future for deep creek lake?");
    images[5] = new Array(520, 523, 526, 529);
    
    var baseIcon = new GIcon(G_DEFAULT_ICON);
    baseIcon.shadow = "http://www.google.com/mapfiles/shadow50.png";
    baseIcon.iconSize = new GSize(20, 34);
    baseIcon.shadowSize = new GSize(37, 34);
    baseIcon.iconAnchor = new GPoint(9, 34);
    baseIcon.infoWindowAnchor = new GPoint(9, 2);
    
    function writeInfo(html){ document.getElementById('info').innerHTML = html; }
    function writeImg(i){ window.open( '/gallery/main.php?g2_view=core.DownloadItem&g2_itemId='+i, "myWindow", "status = 1, height = 510, width = 650, resizable = 0" ); }

    function createMarker(point, map, n) {

        var numIcon = new GIcon(baseIcon);
        numIcon.image = "/media/markers/marker" + (n+1) + ".png";
        var marker = new GMarker(point, { icon:numIcon });
    
        //var marker = new GMarker(point);
        var imgs = images[n];
        GEvent.addListener(marker, 'click', function(){            
            var infohtml = '';
            for(var i = 0; i < imgs.length; i++){
                infohtml += '<a href="javascript:writeImg('+(imgs[i]+1)+')"><img border=0 src="/gallery/main.php?g2_view=core.DownloadItem&g2_itemId='+imgs[i]+'"></a><br>';
            }
            writeInfo(infohtml);
            map.openInfoWindowHtml(point,"<div style='width: 300px;'><h3>"+points[n][2]+"</h3><p>"+points[n][3]+"</p></div>");
        }); 
        return marker;
    }


    function load() {
    
      if (GBrowserIsCompatible()) {
        var map = new GMap2(document.getElementById("map"));
        map.setCenter(new GLatLng(39.45747, -79.30417), 15);
        map.setMapType(G_SATELLITE_MAP);        
        for (var i = 0; i < points.length; i++) {
            var point = new GLatLng(points[i][0], points[i][1]);
            map.addOverlay(createMarker(point, map, i));            
        }
      }
    }
  
   window.onload = load;
   window.onunload = GUnload;
