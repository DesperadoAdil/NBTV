export {
  setSWFIsReady,
  RtmpStreamer,
}
function setSWFIsReady(){alert("test4");isReady||(console.log("swf is ready!"),isReady=!0)}
var isReady=!1;
function RtmpStreamer(elem){alert("test3");isReady=!0;var _elem=elem;isReady||setTimeout(function(){return RtmpStreamer(elem)},1e3),this.publish=function(url,name){_elem.publish(url,name)},this.play=function(url,name){_elem.play(url,name)},this.disconnect=function(){_elem.disconnect()},this.setScreenSize=function(width,height){_elem.setScreenSize(width,height)},this.setScreenPosition=function(x,y){_elem.setScreenPosition(x,y)},this.setCamMode=function(width,height,fps){_elem.setCamMode(width,height,fps)},this.setCamFrameInterval=function(frameInterval){_elem.setCamFrameInterval(frameInterval)},this.setCamQuality=function(bandwidth,quality){_elem.setCamQuality(bandwidth,quality)},this.setMicQuality=function(quality){_elem.setMicQuality(quality)},this.setMicRate=function(rate){_elem.setMicRate(rate)}};
