var HOME_PATH = window.HOME_PATH || '.';

var cityhall = new naver.maps.LatLng(37.8694561,127.7444707),
    map = new naver.maps.Map('map', {
        center: cityhall.destinationPoint(0, 500),
        zoom: 10
    }),
    marker = new naver.maps.Marker({
        map: map,
        position: cityhall
    });

var contentString = [
        '<div class="iw_inner">',
        '   <h3>강원대학교</h3>',
        '   <p>강원도 춘천시 석사동 강원대학길 1<br />',
        '       <img src="https://lh5.googleusercontent.com/p/AF1QipNpemH0S0ktF5LWs9M1AJbhFD0dgUc4ys-7eO1L=w408-h244-k-no" width="55" height="55" alt="강원대학교" class="thumb" /><br />',
        '       033-250-6114 | 학교<br />',
        '       <a href="http://www.kangwon.ac.kr" target="_blank">www.kangwon.ac.kr/</a>',
        '   </p>',
        '</div>'
    ].join('');

var infowindow = new naver.maps.InfoWindow({
    content: contentString
});

naver.maps.Event.addListener(marker, "click", function(e) {
    if (infowindow.getMap()) {
        infowindow.close();
    } else {
        infowindow.open(map, marker);
    }
});

infowindow.open(map, marker);