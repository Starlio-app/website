function load(date) {
    fetch(`https://api.starlio.space/wallpaper/${date}`).then(res => {
        res.json().then(data => {
            if (data.length === 0) return;

            document.querySelector("div.wallpaper img").src = data.url;
            document.querySelector("div.wallpaper div.wallpaper-text div.wallpaper-desc h1").innerHTML = data.title;
            document.querySelector(".copyright").innerHTML = `Image Credit & Copyright: ${data.copyright}`;
            document.querySelector(".desc").innerHTML = data.explanation;
        });
    });
}

function parseURL() {
    let pathname = document.location.pathname
    pathname = pathname.slice(pathname.lastIndexOf('/')+1)

    if (isNaN(new Date(pathname).getTime())) return null;
    if (!isValidDate(pathname)) return null;

    return pathname;
}


/* THX, bro <3
 https://stackoverflow.com/a/35413963/20781634
 */
function isValidDate(dateString) {
  var regEx = /^\d{4}-\d{2}-\d{2}$/;
  if(!dateString.match(regEx)) return false;
  var d = new Date(dateString);
  var dNum = d.getTime();
  if(!dNum && dNum !== 0) return false;
  return d.toISOString().slice(0,10) === dateString;
}

load(parseURL());