  var scale = 1;
  var minScale = 1 ; 
  var maxScale = 1; 
  function zoomIn() {
    if (scale < maxScale) {
      scale *= 1.1;
      if (scale > maxScale) scale = maxScale;
      applyZoom();
    }
  }

  function zoomOut() {
    if (scale > minScale) {
      scale /= 1.1;
      if (scale < minScale) scale = minScale;
      applyZoom();
    }
  }

  function applyZoom() {
    var div = document.getElementById('vacancy-prev');
    div.style.transform = 'scale(' + scale + ')';
  }
  
function progressIn(step){
    var div = document.getElementById('prBar');
    div.style.transition = 'width 0.5s ease-in-out';

    setTimeout(function() {

      switch (step){
        case 1: div.style.width = 33.33 + '%'; break;
        case 2: div.style.width = 66.66 + '%'; break;
        case 3: div.style.width = 100 + '%'; break;
        default: div.style.width = 0 + '%'; break;
      }
        
    }, 300); 
    
}


function disablePagination(){
    div = getElementById('pag');
    div.style.display = 'none';
}

                            

function generateImage() {
  var element = document.getElementById('vacancy-prev');
  
    html2canvas(element, {
      onrendered: function(canvas) {
          var imgData = canvas.toDataURL('image/png');
          document.getElementById('imgData').value = imgData;
          document.getElementById('imgForm').submit();
      }
  });
}




